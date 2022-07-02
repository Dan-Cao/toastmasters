import csv
from pathlib import Path

guestbook_file = Path(__file__).parent.parent / "fixtures/fake_guestbook.csv"
new_header = ["first_name", "last_name", "email", "phone", "registered", "found_us_on"]


def transform_line(guest):
    registration_date = str(guest["registered"]).rsplit(" ", maxsplit=1)[0]
    return [
        guest["first_name"],
        guest["last_name"],
        guest["email"],
        guest["phone"],
        registration_date,
        guest["found_us_on"]
    ]


with guestbook_file.open() as csv_file:
    for line in csv.DictReader(csv_file):
        print(line)
        print(transform_line(line))
