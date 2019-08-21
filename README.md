# Config Loader

Python yaml config loader

# Getting Started

0. Prerequisites
    * [Python](https://www.python.org/) 3.6.x
    * [Pipenv](https://pipenv.readthedocs.io/en/latest/)
    * [Pyenv](https://github.com/pyenv/pyenv) (optional)

1. Install development dependencies:
    ```
    $ pipenv sync --dev
    ```

2.  Run test
    ```
    $ pipenv run pytest
    ```

# Example Usage
    ```
    class AppConfig(BaseConfigLoader):
        prop_str: str
        prop_int: int

    AppConfig(file="values.yaml")

    ```

further example see ExampleConfig.py