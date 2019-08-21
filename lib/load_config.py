import os
from collections import namedtuple

import yaml


class BaseConfigLoader:
    supported_types = [str, int]

    def __init__(self,  **kwargs):
        file_name = kwargs.get("file", "config.yaml")
        print("\n File name:", file_name)
        full_filepath = os.path.join(os.getcwd(), file_name)

        with open(full_filepath, 'r') as file:
            values_dict = yaml.load(file)

        annotations = self.__annotations__
        defined_tuples = []
        for key in annotations.keys():
            print("Anno: ", key)
            key_type = annotations.get(key)
            if key_type is None:
                pass
            elif key_type in self.supported_types:
                self.__setattr__(key, values_dict[key])
            else:
                init_type = key_type
                type_value_dict = {}
                defined_tuples.append(type(init_type).__name__)
                for type_attr in vars(init_type)['_fields']:
                    type_obj_value = values_dict[key][type_attr]
                    print("\n Prop:", type_attr, " Value:", type_obj_value)
                    type_value_dict.update({type_attr: type_obj_value})

                new_obj = namedtuple(type(init_type).__name__, type_value_dict.keys())(*type_value_dict.values())
                self.__setattr__(key, new_obj)
