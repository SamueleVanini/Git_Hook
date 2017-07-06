# Python Comment Counter
Utility to count the comments in the .py files of a Git repository, to check the conformance to a pre-established comment quota.
Python Comment Counter stops the commit if one ore more Python files don't have enough comment lines. Additionally, it checks for pydocs on functions.

# Requirements
This utility requires the module gitpython. You can install it via pip:
`pip install gitpython`
or easy install:
`easy_install gitpython`

# Installation
Simply add the py-comment-counter on the home folder of your Git project (the folder in which the .git hidden directory is located). Navigate in the folder `py-comment-counter\config_script` and check the parameters contained in `config.ini`. Then, execute the script `git_template_conf.cmd`. The script will add a pre-commit hook to Git, so that before every commit the amount of comment lines will be automatically checked for every Python file.
If the pre-commit hook file already contains code, the check will be appended. This does mean that the `git_template_conf.cmd` **must be executed only one time.**