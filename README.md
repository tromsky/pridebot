# pridebot

## Setup

Built with Python 3.10.4 (Optional)

`pyenv install 3.10.4`

Clone this repo

`git clone git@github.com:tromsky/pridebot.git`

Select the Python version (Optional)

`cd pridebot && pyenv local 3.10.4`

Create a virtual environment (Optional)

`python -m venv . --copies && source bin/activate`

Install the requirements

`pip install -r requirements.txt`

Install the dev requirements

`pip install -r dev-requirements.txt`

Create a environment variable to store the API bearer token

`export BEARER_TOKEN="<bearer token>"`

Run the script

`python main.py`
