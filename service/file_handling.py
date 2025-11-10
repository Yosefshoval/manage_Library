import json

class FileHandler:
    
    @staticmethod
    def update_file(data : list, filename):
        
        diict_data = list(map(lambda item : item.__dict__, data))

        json_data = json.dumps(diict_data, indent=3)
        
        with open(filename, 'w') as file:
            file.write(json_data)

