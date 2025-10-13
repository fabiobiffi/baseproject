#!/usr/local/bin/python

import os
import sys
result = os.system('uv run ruff check --fix src/')

if result > 0:
    os.system('uv run ruff format src/')
    print("⚠️ Reformatted files -> add them to GIT")
    sys.exit(1)
else:
    result = 0
    result += os.system("uv run pylint --load-plugins pylint_django --django-settings-module=baseproject.settings --rc-file .pylintrc src/")
    result += os.system("uv run pytest tests/")

    if result > 0:
        sys.exit(2)

print("✅ All tests passed !!!")
sys.exit(0)
