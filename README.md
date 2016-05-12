# AnsiblePlaybookCleaner
Web application that dynamically refractors bad playbooks into good

## Usage

Launching the `playbookCleaner.py` file independently will start a publicly available web server on port 8080. You can use the software by accessing the hosted page.

The web app is best used as a uwsgi app behind a proxy like nginx.

## Screen Shots

Step 1.
Paste in your bad playbook
![ScreenShot](https://raw.githubusercontent.com/mholiv/AnsiblePlaybookCleaner/devel/meta/img/shot1.png)

Step 2.
Click Refactor and view the results
![ScreenShot](https://raw.githubusercontent.com/mholiv/AnsiblePlaybookCleaner/devel/meta/img/shot2.png)

## Recommendations

The app was written on and was designed for pypy3. Other implications of python will most likely work if the prerequisites are available, but this is not tested.

## Known Bugs

The app does not preserve comments.

## Requirements
- pypy3 or other implementations of python 3.2.5 or later
- flask 0.10.1. or later
- PyYAML 3.11 or later

## Author
AnsiblePlaybookCleaner was written by Caitlin Campbell. You can reach her at cacampbe/redhat/com