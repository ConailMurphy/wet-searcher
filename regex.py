#!/usr/bin/python

#   to do
# look for "WARC-Target-URI:" then store the url that follows
# if we find a match with our regex, do something with the stored url
# keep searching for matches afterwards
# after we fin two blank lines in a row, or WARC/1.0, we know we have reached the data for a new page
# look for "WARC-Target-URI:" and replace the old url

import re
import os
import sys
import codecs

myInputFile = sys.argv[1]  # gets a file name from first command line argument
myRegexFile = sys.argv[2]  # gets a file name from the second command line argument

if os.path.exists(myInputFile):  # check if the input file exists
    print "Input File exists"
    inputFileName = myInputFile

    if os.path.exists(myRegexFile):  # check if the regex pattern file exists
        print "Regex File exists"
        regexFileName = myRegexFile

        count = 0  # used to count total positive matches
        lines = 0  # used to count how many lines of the input file have been read

        expressions = open(regexFileName).readlines()  # create a list of expressions to search for such that
        # each entry in the list is a line of the regex file

        f = codecs.open(inputFileName, encoding='utf-8')  # opens the  input file with utf-8 encoding so it can handle
        # non-standard characters, mainly for foreign languages
        # eg. cyrillic arabic etc.

        for line in f:
            lines += 1
            for ex in expressions:
                matchObj = re.match(ex, line, re.IGNORECASE)
                if matchObj:
                    count += 1
        f.close()

        print  "%i lines read" % lines

        if count == 0:
            print "No matches!"

        else:
            print "%i matches" % count
    else:
        print "No regex file found"
else:
    print "No input file found"
