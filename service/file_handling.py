import json

class FileHandler:
    
    @staticmethod
    def update_file(data : list, filename):
        
        dict_data = list(map(lambda item : item.__dict__, data))

        json_data = json.dumps(dict_data, indent=3)
        
        with open(f'../data/{filename}.json', 'w') as file:
            file.write(json_data)

