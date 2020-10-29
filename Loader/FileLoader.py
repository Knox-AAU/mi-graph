import os
import json
from Resources.JsonWrapper import Content




def load_json_file(path: str) -> Content:
    if os.stat(path).st_size > 0:

        with open(path, 'r', encoding='utf8') as file:
            data = json.load(file)

        return Content(data['properties']['content']['properties'])

    else:
        raise IOError
