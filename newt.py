#!/usr/bin/env python3

import sys, getopt, os
from shutil import copyfile

def main(argv):

    if os.environ['NEWT_TEMPLATE_PATH'] == '':
        template_path = "/opt/newt/templates"
    else:
        template_path = os.environ['NEWT_TEMPLATE_PATH']

    template = ''
    filename = ''

    EXECUTABLE = False

    try:
        opts, args = getopt.getopt(argv,"ht:xo:",["template=","output="])
    except getopt.GetoptError:
        print('newt -t <template> [-o <outputfile>] [-x]')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('newt -t <template> [-o <outputfile>] [-x]')
            sys.exit()
        elif opt in ("-t", "--template"):
            template = arg
        elif opt in ("-o", "--output"):
            filename = arg
        elif opt in ("-x"):
            EXECUTABLE = True

        if template == '':
            print('newt -t <template> [-o <outputfile>] [-x]')
            sys.exit(2)

        if filename == '':
            filename = template

    available_templates = {
        'c':'.c',
        'python2':'.py',
        'python3':'.py',
        'bash':'.sh' 
        }


    if template not in available_templates:
        print("ERROR: Template not found.")
        sys.exit(2)

    try:
        #tf = open(template_path+"/"+template+".template","r")
        full_template_filename = template_path+"/"+template+".template"
        extension = available_templates[template]
        copyfile(full_template_filename,filename+extension)
        if EXECUTABLE:
            os.chmod(filename+extension,0o755)
    except:
        print("ERROR: Could not access "+full_template_file)
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])
