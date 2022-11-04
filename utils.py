from os import path

def get_config_file(json_config = None):
    '''Try to get json config file by his absolutes path not relative ./path_to/... 
    
    We Assume that config file existe in the directory
    '''

    if not json_config:
        raise FileExistsError('<FileExistsError>: Please enter a valide file name.')

    file = path.abspath(__file__)
    directory = path.dirname(file)
    return path.join(directory, json_config)



def generate_reference(database='database', path=''):
    """generate path, for split path by slash (/) and retun a collection or document

    attributes:
        path: string that containe path of document or collection (collection/document/collection/document)

    """
    parts = path.split("/")
    reference = database
    for index, part in enumerate(parts):
        if index % 2 == 0:
            reference += f".collection('{part}')"
        else:
            reference += f".document('{part}')"

    return reference
