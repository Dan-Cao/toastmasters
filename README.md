# Toastmasters related tools

## Setup

Create virtual environment

```commandline
python -m venv tm-venv
.\tm-venv\Scripts\Activate.ps1
pip install requirements.txt
```

Create secrets file - copy `secrets-sample.json` and name it `secrets.json`, and add your ToastHost email and password

## Getting Toasthost guests

With the virtual environment active:
```commandline
python .\spikes\get_guestbook.py
```

This will give the guestbook in CSV format - you can copy this to Excel using the [Text Import Wizard](https://support.microsoft.com/en-us/office/text-import-wizard-c5b02af6-fda1-4440-899f-f78bafe41857):
* Select Comma for the Delimiter
* Change the Column data format for the phone number to Text, and the date to Date