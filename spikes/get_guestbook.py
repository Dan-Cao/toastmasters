"""
Usage:
python spikes/get_guestbook.py > out.csv
"""
import csv
import json
import sys

from pathlib import Path

import requests
from bs4 import BeautifulSoup

secrets_file = Path(__file__).parent.parent / "secrets.json"
secrets = json.loads(secrets_file.read_text())

session = requests.session()

# open sign in form
response = session.get("https://toasthost.co.uk/signIn")
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

csrf_token_elements = soup.find_all("input", attrs={"name": "csrfToken"})
assert len(csrf_token_elements) == 1
csrf_token = csrf_token_elements[0].get("value")

# sign in
data = {
    "csrfToken": csrf_token,
    "email": secrets["toasthost_email"],
    "password": secrets["toasthost_password"],
    "submit": ["submit"]
}
response = session.post("https://toasthost.co.uk/signIn", data=data)
response.raise_for_status()

# get guestbook
response = session.get("https://toasthost.co.uk/club/londonvictorians/guestbookManagement")
soup = BeautifulSoup(response.text, "html.parser")

tables = soup.find_all("table", attrs={"id": "data"})
assert len(tables) == 1
table = tables[0]

# parse guest book to csv
new_header = ["first_name", "last_name", "email", "phone", "registered", "found_us_on"]
writer = csv.writer(sys.stdout, lineterminator="\n")
writer.writerow(new_header)


def process_row(table_row):
    cells = table_row.find_all("td")
    cell_contents = [c.text for c in cells]

    first_name = cell_contents[0]
    last_name = cell_contents[1]
    email = cell_contents[2]
    phone = cell_contents[3]
    registered = cell_contents[4]
    registered = str(registered).rsplit(" ", maxsplit=1)[0]
    found_us_on = cell_contents[6]

    writer.writerow([first_name, last_name, email, phone, registered, found_us_on])


for row in table.tbody.find_all("tr"):
    process_row(row)
