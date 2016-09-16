#!/usr/bin/env python
"""
SYNOPSIS

    retire.apk [-f --file] APK filename

DESCRIPTION

    This looks up the libraries in the APK and compares them to vulnerable package lists.

EXAMPLES

    python retire.apk.py [-f --file] filename

AUTHOR

    Bill Sempf, bill@pointweb.net

VERSION

    0.1.1.0

REFERENCE



"""
import sys
import os
import traceback
import optparse
import time
import zipfile
import csv
import operator
import re
import codecs




def main():

    global options, args

    with zipfile.ZipFile(options.file, 'r') as apkFile:
        apkFiles = apkFile.namelist
        for p in apkFiles(): print p

if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(), usage=globals()['__doc__'], version='$Id$')
        parser.add_option ('-f', '--file', type="str",  help='file name')
        parser.add_option ('-v', '--verbose', type="str",  help='verbose handling')
        (options, args) = parser.parse_args()
        #if len(args) < 1:
        #    parser.error ('missing argument')
        if options.verbose: print time.asctime()

        main()

        if options.verbose: print time.asctime()
        if options.verbose: print 'TOTAL TIME IN MINUTES:',
        if options.verbose: print (time.time() - start_time) / 60.0
        sys.exit(0)
    except KeyboardInterrupt, e: # Ctrl-C
        raise e
    except SystemExit, e: # sys.exit()
        raise e
    except Exception, e:
        print 'ERROR, UNEXPECTED EXCEPTION'
        print str(e)
        traceback.print_exc()
        os._exit(1)

