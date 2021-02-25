import difflib
import string
import time
from typing import List, Tuple

import requests
import typer
from bs4 import BeautifulSoup
from timeout_decorator import timeout
from twilio.rest import Client as TwilioClient

ERROR_TEXTS = (
    "We're Sorry! An Error Occurred.",
    "The server is temporarily unable to service your request",
    "Oops, I guess we weren't so genius",
)
PUNCTUATION_TABLE = str.maketrans("", "", string.punctuation)


def alert(twilio_client, from_phone: str, to_phones: List[str], body: str) -> None:
    for phone in to_phones:
        twilio_client.api.account.messages.create(to=phone, from_=from_phone, body=body)


@timeout(5)
def _website_text(website: str) -> Tuple[str, str]:
    response = requests.get(website)
    response.raise_for_status()

    text = BeautifulSoup(response.text, features="lxml").get_text()
    for error_text in ERROR_TEXTS:
        if error_text in text:
            raise ValueError("Contains Error Text")

    return (
        text,
        "".join(filter(bool, text.split()))
        .translate(PUNCTUATION_TABLE)
        .lower()
        .replace(" ", "")
        .replace("cst", "pst")
        .replace("mst", "pst")
        .replace("est", "pst"),
    )


def website_text(website: str) -> Tuple[str, str]:
    """Returns either the text from the website (along side a normalized form),
    or two empty strings on any error.
    """
    try:
        return _website_text(website)
    except Exception:
        return ("", "")


def alert_on_change(
    twilio_account_id: str,
    twilio_token: str,
    twilio_phone: str,
    website: str,
    alert_phones: List[str],
    check_every_seconds: int = 2,
    error_backoff: int = 30,
):
    twilio = TwilioClient(twilio_account_id, twilio_token)
    original = current = website_text(website)
    while not current[1] or original[1] == current[1]:
        if not current[1]:
            print("E", end="", flush=True)
            time.sleep(error_backoff)
        else:
            print(".", end="", flush=True)

        current = ("", "")
        while not current[1]:
            try:
                current = website_text(website)
            except Exception:
                print("E", end="", flush=True)
                time.sleep(error_backoff)
        time.sleep(check_every_seconds)

    for line in difflib.context_diff(original[0].splitlines(), current[0].splitlines()):
        print(line)

    alert(twilio, twilio_phone, alert_phones, website)


def main():
    typer.run(alert_on_change)
