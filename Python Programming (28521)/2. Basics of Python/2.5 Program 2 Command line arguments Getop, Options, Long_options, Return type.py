# Command line arguments Getop, Options, Long_options, Return type
# Python program to demonstrate
# command line arguments
import getopt, sys
# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]
# Options
options = "hom:"
# Long options
long_options = ["Help", "My_file", "Output="]
try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)

    # checking each argment
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-h", "--Help"):
            print("Displaying Help")
        elif currentArgument in ("-m", "--My_file"):
            print("Displayig file_name:",sys.argv[0])
        elif currentArgument in ("-o", "--Output"):
            print(("Enabling special output mode(% s)")%(currentValue))
except getopt.error as err:
    # output error, and return with an error code
    print(str(err))
