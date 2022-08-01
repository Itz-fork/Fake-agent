# Copyright (c) 2022 Itz-fork

import os
import requests

from enum import Enum
from json import loads
from random import choice
from .types import Browsers


class Fake_Agent:
    """
    Fake_Agent class

    ### Arguments

        - `browser` :Enum (optional) - Enum of the rowser that you want to use (from FakeAgent.types import Browsers)
        - `load_on_init` :bool (optional) - Whether you want to load json file to memory on init
    """

    def __init__(self, browser: Enum = Browsers.FIREFOX, load_on_init: bool = True) -> None:
        self.browser = browser
        # Json file
        self.data_location = f"{os.path.dirname(__file__)}/data/"
        self.json_file = None
        if load_on_init:
            self.json_file = self._read_json_as_dict(
                f"{self.data_location}{self.browser.value}.json")

    def get(self, browser: Enum = None, as_gen: bool = False):
        """
        Get user agents as a list or generator according to the browser that `Fake_Agent` class initialized with

        ### Arguments

            - `browser` :Enum (optional) - Enum of the browser you want to get user agents. Defaults to the browser that Fake_Agent class initialized with
            - `as_gen` :bool (optional) - Return value as a generator rather than a list. Defaults to `False`
        """
        to_use = browser.value if browser else self.browser.value
        vl = self.json_file if (self.browser == browser and self.json_file) else self._read_json_as_dict(
            f"{self.data_location}{to_use}.json")
        if as_gen:
            return (val for val in vl.values())
        else:
            return [val for val in vl.values()]

    def random(self, mix_browsers: bool = True, with_details: bool = False):
        """
        Randomly select user agent

        ### Arguments

            - `mix_browsers` :bool (optional) - To randomly select a browser. Defaults to `True`
            - `with_details` :bool (optional) - To get user agent details. Defaults to False (INTERNET REQUIRED)
        """
        brdict = self._read_json_as_dict(
            f"{self.data_location}{choice(self._get_supported_browsers())}.json") if mix_browsers else self.json_file
        chosen = choice(list(brdict.values()))
        return self.get_ua_details(chosen) if with_details else chosen

    def chrome(self, is_random: bool = False, as_gen: bool = False):
        """
        Get chrome user agents as a list or generator

        ### Arguments

            - `is_random` :bool (optional) - Return a random user agent. Defaults to `False`
            - `as_gen` :bool (optional) - Return value as a generator rather than a list. Defaults to `False`
        """
        ual = self.get(Browsers.CHROME, as_gen)
        return choice(list(ual)) if is_random else ual

    def firefox(self, is_random: bool = False, as_gen: bool = False):
        """
        Get firefox user agents as a list or generator

        ### Arguments

            - `is_random` :bool (optional) - Return a random user agent. Defaults to `False`
            - `as_gen` :bool (optional) - Return value as a generator rather than a list. Defaults to `False`
        """
        ual = self.get(Browsers.FIREFOX, as_gen)
        return choice(list(ual)) if is_random else ual

    def edge(self, is_random: bool = False, as_gen: bool = False):
        """
        Get edge user agents as a list or generator

        ### Arguments

            - `is_random` :bool (optional) - Return a random user agent. Defaults to `False`
            - `as_gen` :bool (optional) - Return value as a generator rather than a list. Defaults to `False`
        """
        ual = self.get(Browsers.EDGE, as_gen)
        return choice(list(ual)) if is_random else ual

    def opera(self, is_random: bool = False, as_gen: bool = False):
        """
        Get opera user agents as a list or generator

        ### Arguments

            - `is_random` :bool (optional) - Return a random user agent. Defaults to `False`
            - `as_gen` :bool (optional) - Return value as a generator rather than a list. Defaults to `False`
        """
        ual = self.get(Browsers.OPERA, as_gen)
        return choice(list(ual)) if is_random else ual

    def safari(self, is_random: bool = False, as_gen: bool = False):
        """
        Get safari user agents as a list or generator

        ### Arguments

            - `is_random` :bool (optional) - Return a random user agent. Defaults to `False`
            - `as_gen` :bool (optional) - Return value as a generator rather than a list. Defaults to `False`
        """
        ual = self.get(Browsers.SAFARI, as_gen)
        return choice(list(ual)) if is_random else ual

    def internet_explorer(self, is_random: bool = False, as_gen: bool = False):
        """
        Get internet explorer user agents as a list or generator

        ### Arguments

            - `is_random` :bool (optional) - Return a random user agent. Defaults to `False`
            - `as_gen` :bool (optional) - Return value as a generator rather than a list. Defaults to `False`
        """
        ual = self.get(Browsers.IE, as_gen)
        return choice(list(ual)) if is_random else ual

    def _get_supported_browsers(self):
        return [v.value for k, v in Browsers.__dict__.items() if k.isupper()]

    def get_ua_details(self, ua: str):
        """
        Get details of an user agent

        ### Arguments

            - `ua` :str - User agent
        """
        resp = requests.get(
            f"http://useragentstring.com/?uas={ua}&getJSON=all").json()
        resp["agent"] = ua
        return resp

    def _read_json_as_dict(self, path: str) -> dict:
        with open(path, "r") as r:
            return loads(r.read())
