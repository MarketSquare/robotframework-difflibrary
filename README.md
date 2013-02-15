[![Build Status](https://travis-ci.org/bulkan/robotframework-difflibrary.png?branch=master)](https://travis-ci.org/bulkan/robotframework-difflibrary)

DiffLibrary is a [Robot Framework](http://code.google.com/p/robotframework/)
test library that will provide keyword functionality to _diff_ two files together

Install
=======

Install robotframework-difflibrary

    pip install -U robotframework-difflibrary


Usage
=====


<table border=1>
    <tr>
        <td>Settings</td>
    </tr>
    <tr>
        <td> Library </td>
        <td> DiffLibrary</td>
    </tr>

    <tr>
        <td>Test Cases</td>
    </tr>

    <tr>
        <td> Diff Two identical files </td>
    <tr>
        <td></td>
        <td> Diff Files  </td>
        <td>loremipsum.txt  </td>
    </tr>
</table>


DiffLibrary uses the external diff executable that is avaible on most Linux systems
out of the box. It also comes packaged with GNU diff binaries for Windows. This is to
work around the problem described in the following issue;

http://code.google.com/p/robotframework/issues/detail?id=497
