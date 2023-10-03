#!/usr/local/bin/python

import os
import sys
result = os.system('black src/ --check')

if result > 0:
    os.system('black src/')
    print("Reformatted files -> add them to GIT")
    sys.exit(1)
else:
    pylint_result = os.system("pylint --load-plugins pylint_django --django-settings-module=baseproject.settings --rc-file .pylintrc src/")

    if pylint_result > 0:
        sys.exit(2)

sys.exit(0)
