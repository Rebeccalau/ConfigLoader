from ExampleConfig import ExampleConfig


def test_load_config_maps_single_property():
    config = ExampleConfig(file="test_config.yaml")

    assert config.property_name == "property_name_str"


def test_load_config_obj():
    config = ExampleConfig(file="test_config.yaml")

    assert config.namedtuple_config.name == "nt_name"
    assert config.namedtuple_config.address == "nt_address"
    assert config.namedtuple_second_config.username == "nt_username"
    assert config.namedtuple_second_config.password == "nt_password"


def test_load_config_without_db_config():
    config = ExampleConfig(file="test_config_without_db.yaml")

    assert config.namedtuple_config.name == "nt_name"
    assert config.namedtuple_config.address == "nt_address"

# diff types - currently setting as string

# def test_config_throws_error_on_load_when_no_namedtuple_values_provided
