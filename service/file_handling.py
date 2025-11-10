import json

class FileHandler:
    
    @staticmethod
    def update_file(data : list, filename):
        
        diict_data = list(map(lambda item : item.__dict__, data))

        json_data = json.dumps(diict_data, indent=3)
        
        with open(filename, 'w') as file:
            file.write(json_data)

    @staticmethod
    def read_file(data_type, object):
        list_class = []
        with open(f"../data/{data_type}.json", 'r') as file:
            dict_file = json.load(file)
            for item in dict_file:
                list_class.append(object(**item))
        return list_class