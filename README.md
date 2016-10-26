[![Build Status](https://travis-ci.org/bulkan/robotframework-difflibrary.png?branch=master)](https://travis-ci.org/bulkan/robotframework-difflibrary)
[![PyPi downloads](https://img.shields.io/pypi/dm/robotframework-requests.svg)](https://pypi.python.org/pypi/robotframework-difflibrary)
[![Latest Version](https://img.shields.io/pypi/v/robotframework-requests.svg)](https://pypi.python.org/pypi/robotframework-difflibrary)



DiffLibrary is a [Robot Framework](http://code.google.com/p/robotframework/)
test library that will provide keyword functionality to _diff_ two files together

Install
=======

Install robotframework-difflibrary

    pip install -U robotframework-difflibrary

Documentation
=============
Documentation for Keywords avaliable here https://bulkan.github.io/robotframework-difflibrary/

Usage
=====

|                           |              |                 |                 |
| :------------------------ | :----------- | :-------------- | :-------------- |
| Settings                  |              |                 |                 |
| Library                   | DiffLibrary  |                 |                 |
| Test Cases                |              |                 |                 |
| Diff Two Identical Files  |              |                 |                 |
|                           | Diff Files   | loremipsum.txt  | loremipsum.txt  |


DiffLibrary uses the external diff executable that is avaible on most Linux systems
out of the box. It also comes packaged with GNU diff binaries for Windows. This is to
work around the problem described in the following issue;

http://code.google.com/p/robotframework/issues/detail?id=497

Docs updation
=============

```Bash
python -m robot.libdoc src/DiffLibrary/ doc/DiffLibrary.html
```
