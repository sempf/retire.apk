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
import re




def main():

    global options, args

    with zipfile.ZipFile(options.file, 'r') as apkFile:
        apkFiles = apkFile.namelist
        # Now I have a list of the files.
        # It is big.
        # I need to filter it based on the regex in the json file
        # Let's start with one regex
        regex = re.compile(r'freetype1')
        match = filter(regex.search, apkFiles)
        for p in match: print(p)

if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(), usage=globals()['__doc__'], version='$Id$')
        parser.add_option ('-f', '--file', type="str",  help='file name')
        parser.add_option ('-v', '--verbose', type="str",  help='verbose handling')
        (options, args) = parser.parse_args()
        #if len(args) < 1:
        #    parser.error ('missing argument')
        if options.verbose: print(time.asctime())

        main()

        if options.verbose: print(time.asctime())
        if options.verbose: print('TOTAL TIME IN MINUTES:')
        if options.verbose: print (time.time() - start_time) / 60.0
        sys.exit(0)
    except KeyboardInterrupt as e: # Ctrl-C
        raise e
    except SystemExit as e: # sys.exit()
        raise e
    except Exception as e:
        print('ERROR, UNEXPECTED EXCEPTION')
        print(str(e))
        traceback.print_exc()
        os._exit(1)

