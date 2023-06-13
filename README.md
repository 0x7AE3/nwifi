# nwifi
A tool to count the number of hosts connected to your ARRIS router (at least most modern ones).

![Demo](nwifi.gif)

## Requirements
- [Chrome Driver](https://chromedriver.chromium.org/downloads) version 103+ (comes with chrome)
- Python 3
- packages listed in requirements.txt

## Virtual Environment 
I recommend doing all of this inside a `virtualenv`, i.e. running the following commands inside an empty directory:
```
python -m venv venv
source venv/bin/activate
```
and you can of course leave the environment at any time by running
```
deactivate
```

## Usage
1. Install the required packages
```
pip install -r requirements.txt
```
2. Adjust `NETWORK_SSID` appropriately (and `5G_PRESENT` if you do not have 5G support) in `config.py`

3. Run the script
```
python main.py
```

## Add to your path
You can clone this project inside your `/usr/local/bin` and then create an `nwifi` executable file there invoking the above command (with a bit of finicking if you used a `venv`).
