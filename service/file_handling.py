import json
from pathlib import Path

filePache = Path(__file__).resolve().parent.parent
print(filePache)

class FileHandler:
    
    @staticmethod
    def update_file(data : list, filename):

        try:
            dict_data = list(map(lambda item : item.__dict__, data))
   
            json_data = json.dumps(dict_data, indent=3)

            with open(f'{filePache}/data/{filename}.json', 'w') as file:
                file.write(json_data)

        except Exception as e:
            print(f'Error updating file: {e}')

    @staticmethod
    def read_file(data_type, object):
        try:
            list_class = []
            with open(f"{filePache}/data/{data_type}.json", 'r') as file:
                dict_file = json.load(file)
                if not dict_file:
                    print(f'There is no contennt in {data_type}')
                for item in dict_file:
                    list_class.append(object(**item))
            return list_class
        except Exception as e:
            print(f'Error reading file: {e}')
        
