import os
from typing import List
from datetime import datetime

from pytz import timezone
import requests

from config import token, year

DATADIR = 'data'
AOC_URL = 'https://adventofcode.com'
COOKIES = {"session": token}

utc = timezone('UTC')
est = timezone('US/Eastern')


def _get_filename(day: int) -> str:
    return os.path.join(DATADIR, f'day_{day:02}.txt')


def _get_url(day: int, suffix: str = 'input') -> str:
    return f'{AOC_URL}/{year}/day/{day}/{suffix}'


def load():
    now_utc = utc.localize(datetime.utcnow())
    now_est = est.normalize(now_utc)

    if now_est.year < 2020:
        current_day = now_est.day
    else:
        current_day = 25

    for day in range(1, current_day+1):
        filename = _get_filename(day)
        if not os.path.exists(filename):
            url = _get_url(day)
            try:
                response = requests.get(url, cookies=COOKIES)
                if not response.ok:
                    raise Exception(f'Data request returned code {response.status_code} with answer {response.text}!')
                with open(filename, 'w') as file:
                    file.write(response.text)
            except Exception as ex:
                raise ex


def get_input(day: int) -> List[str]:
    filename = _get_filename(day)
    with open(filename, 'r') as file:
        content = file.read()

    return content.splitlines()


def submit(value, day: int, level: int = 1):
    url = _get_url(day, 'answer')
    response = requests.post(
        url=url,
        cookies=COOKIES,
        data={"level": level, "answer": value},
    )
    if not response.ok:
        raise Exception(f'Submit request returned code {response.status_code} with answer {response.text}!')

    if 'That\'s the right answer!' in response.text:
        return True
    elif 'Did you already complete it' in response.text:
        return True
    elif 'That\'s not the right answer' in response.text:
        return False
    else:
        print(response.text)
        raise ValueError('Could not determine if right or wrong answer!')


# Always make sure all available files are there
load()
