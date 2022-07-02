import csv
import sys
from pathlib import Path

import click

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


@click.command()
@click.argument("in_file", type=click.File("r"))
def parse_guestbook(in_file):
    """Usage:

    python .\scripts\parse_guestbook.py fixtures/fake_guestbook.csv > out.csv
    """

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow(new_header)

    for line in csv.DictReader(in_file):
        writer.writerow(transform_line(line))


if __name__ == "__main__":
    parse_guestbook()
