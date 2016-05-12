# Ansible-Cleanup
A simple way to refactor ansible playbooks

## Screen Shots

Step 1.
Paste in the x=y style playbook
![ScreenShot](https://raw.githubusercontent.com/mholiv/AnsiblePlaybookCleaner/master/meta/img/shot1.png)

Step 2.
Click Refactor and view the results
![ScreenShot](https://raw.githubusercontent.com/mholiv/AnsiblePlaybookCleaner/master/meta/img/shot2.png)

## Recommendations

The app was written on and was designed for pypy3. Other implications of python will most likely work if the prerequisites are available, but this is not tested.

##  General Usage

Launching the `playbookCleaner.py` file independently will start a publicly available web server on port 5000. You can use the software by accessing the hosted page.

The web app is best used as a uwsgi app behind a proxy like nginx.

## Setup & Usage (GNU/Linux & OS X)

This guide assumes the virtualenv, pip and, pypy3 packages are installed. If they are not consult your operating system's documentation on how to install them. 

1. Set up the virtual python environment
`mkdir Ansible-Cleanup`

2. Create the virtual environment
`virtualenv -p pypy3 Ansible-Cleanup`

3. Enter and activate the virtual environment
`cd Ansible-Cleanup`
`source bin/activate`

4. Download Ansible-Cleanup
`git clone https://github.com/mholiv/Ansible-Cleanup.git`

5. Install the Ansible-Cleanup Prerequisites
`pip install -r Ansible-Cleanup/source/requirements.txt`

6. Edit the `Ansible-Cleanup/source/settings.yml` file. Be sure to replace the secret key with a randomly generated hex string.

7. Launch the Ansible-Cleanup web server
`cd Ansible-Cleanup/source/`
`pypy3 playbookCleaner.py`

8. A web server will launch on port 5000. You can access it at http://127.0.0.1:5000

Note: In order to launch the web server in the future you will need to reactivate the virtual environment.
## Known Bugs

- The app does not preserve comments.
- The ordering of elements is subject to change

## Upcoming Features
- Comment Preservation
- The ability to specify element ordering weight

## Requirements
- pypy3 or other implementations of python 3.2.5 or later
- flask 0.10.1. or later
- PyYAML 3.11 or later

## Author
Ansible-Cleanup was written by Caitlin Campbell. You can reach her at cacampbe/redhat/com
