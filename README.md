# Research Group tool down checker
This repository contains a simple script for checking whether a web service returns an OK status,
and restarting apache if it doesn't.

The script sends a HTTP request every hour to the url specified in `config.ini`, and if the response code is
`>=400` then the script will issue an apache web server restart command to the system.

You can change which url a request is sent to by changing the `url` parameter in `config.ini`.
For example, if you want to know if Tranport Access Tool is down or not:
```ini
[url]
url=https://transport-access-tool.dcs.warwick.ac.uk/
```

## Installation
1. Create a python virtual environment `python -m venv venv`
2. Activate it using `source venv/bin/activate`
3. Install requirements `pip install -r requirements.txt`
3. Set the URL in `config.ini` to the desired tools.

## Running
1. Start a tmux session (or use `nohup`) to prevent disconnect signals from killing the process.
2. Activate the environment using `source venv/bin/activate`
3. Run the script.
