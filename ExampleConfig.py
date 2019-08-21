from typing import NamedTuple

from lib.load_config import BaseConfigLoader


class nt_config(NamedTuple):
    name: str
    address: str


class nt2_config(NamedTuple):
    password: str
    username: str


class ExampleConfig(BaseConfigLoader):
    property_name: str

    namedtuple_config: nt_config

    namedtuple_second_config: nt2_config
