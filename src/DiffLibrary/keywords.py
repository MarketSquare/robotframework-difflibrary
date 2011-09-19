import sys
import os

import subprocess


from robot.libraries.BuiltIn import BuiltIn

class DiffKeywords(object):
    ROBOT_LIBRARY_SCOPE = 'Global'

    root = os.path.abspath(os.path.join(__file__, '..'))


    def __init__(self):
        self.builtin = BuiltIn()


    def _getdiff(self):
        ''' returns path to diff depending on platform '''

        diff = 'diff --strip-trailing-cr'
        if 'win' in sys.platform:
            diff = "%s --strip-trailing-cr " %os.path.join(self.root, 'bin', 'diff', 'diff.exe')
        return diff

    
    def _getndiff(self):
        raise Exception("Not implemented")


    def _newdiff(self, actfile, reffile, diff_func='_getdiff', diff_params=None, diff_file_path=None, filter=None):
        ''' compare two sxv4dump files

        *actfile:* sxv4dump file created in latest build

        *reffile:* reference sxv4dump file, gzipped

        *diff_file_path:* absolute path of directory to save the diff delta

        *diff_cmd:* custom diff command'''

        diff_types = {'_getdiff': self._getdiff, '_getndiff': self._getndiff}
        diff_lines = {'_getdiff': 2, '_getndiff': 4}

        for file in (actfile, reffile):
            if not os.path.exists(file):
                self.builtin.fail("%s doesn't exist" %file)

        #act_md5 = reffile.replace('.gz', '') + '.md5'
        #md5_cmd = '%s "%s"' %(self._getmd5(), actfile)

        #new_md5hash = None
        ## write out the md5 hash to correct file ?
        #save_md5_hashes = False
        #try:
        #    save_md5_hashes = self.builtin.replace_variables('${SAVE_MD5_HASH}')
        #except:
        #    pass

        ## write out the md5sum to the correct file ?
        #if self.builtin.convert_to_boolean(save_md5_hashes):
        #    try:
        #        fmd5 = open(act_md5, 'w')
        #        # have we already calculated md5 hash ?
        #        if not new_md5hash:
        #            new_md5hash, rc = self._run(md5_cmd)
        #        if new_md5hash[0] == '\\': new_md5hash = new_md5hash[1:]
        #        fmd5.write(new_md5hash)
        #        fmd5.close()
        #    except Exception, e:
        #        print "*WARN*: Failed to create md5 file"
        #        print "*INFO* "
        #        raise

        ## reference md5 hash file exists
        #if os.path.exists(act_md5):
        #    ref_md5hash = open(act_md5).read().split()[0]

        #    if not new_md5hash: new_md5hash, rc = self._run(md5_cmd)
        #    if new_md5hash[0] == '\\': new_md5hash = new_md5hash[1:]

        #    # md5 hashes match no need to do the diff
        #    if ref_md5hash == new_md5hash.split()[0]: 
        #        print 'md5 hashes match\n%s\n%s' %(ref_md5hash, new_md5hash.split()[0])
        #        return


        # the reference file is gzip'ed
        tempfile = None
        #if reffile.endswith('gz'):
        #    # unzip the gzip file into a temporary file
        #    tempfile = NamedTemporaryFile(delete=False, dir=self.get_temp_dir())
        #    for l in gzip.open(reffile).readlines():
        #        tempfile.write(l.replace('\r\n', '\n'))
        #    tempfile.close()
        #    print "tempfile: ", tempfile.name
        #    reffile = tempfile.name


        # construct the diff command
        diff_function = diff_types.get(diff_func, '_getdiff')
        if diff_params != None:
            diff_cmd = '%s %s "%s" "%s"' %(diff_function(), diff_params, actfile, reffile)
        else:
            diff_cmd = '%s "%s" "%s"' %(diff_function(), actfile, reffile)
        output, rc = self._run(diff_cmd)

        lines = output.splitlines()

        # code 127 shows that shell hasn't found the command
        if rc == 127: 
            self.builtin.fail(output)
        else:
            if diff_func == '_getdiff':
                if rc == 2 or len(lines) == 1: 
                    self.builtin.fail(output)

        # remove the temp file afterwards
        if tempfile: os.remove(tempfile.name)

        # filter the diff output
        if filter:  lines = filter(output.splitlines())

        # if there is no differences there will still be some lines remaining 
        # because the filter will remove the timestap diff's
        lines_to_skip = diff_lines.get(diff_func, '_getdiff')
        if lines and len(lines) > lines_to_skip:
            print '\n'.join(lines)
            self.builtin.fail("differences found between %s and %s" %(actfile, reffile))



    def diff_files(self, file1, file2, fail=True):
        ''' Diff two text files

        `file1`: absolute path to the first first file

        `file2`: absolute path to the first second file

        `fail`:  If there are differences it will throw an exception and test will fail
                 defaults to True, if False test's will continue '''

        self.builtin.log("file1: %s" %file1)
        self.builtin.log("file2: %s" %file2)

        fail = self.builtin.convert_to_boolean(fail)
        if fail:
            self._newdiff(file1, file2)
        else:
            try:
                self._newdiff(file1, file2)
            except Exception, e:
                self.builtin.log(e)


    def _run(self, cmd):
        ''' internal run command '''

        if not cmd: return

        self.builtin.log(cmd)
        #cmd = process_cmd(cmd)

        # run the given command in a child shell process (cmd.exe on win and sh/bash on *nix)
        self.cmd = subprocess.Popen(cmd + ' 2>&1', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        # it will block here and try to read everything into memory
        output = self.cmd.communicate()[0]

        return output, self.cmd.wait()



if __name__ == "__main__":
    d = DiffKeywords()
    print d.getdiff()
