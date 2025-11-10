import json

class FileHandler:

    @staticmethod
    def read_file(data_type, object):
        list_class = []
        with open(f"../data/{data_type}.json", 'r') as file:
            dict_file = json.load(file)
            for item in dict_file:
                list_class.append(object(**item))
        return list_class