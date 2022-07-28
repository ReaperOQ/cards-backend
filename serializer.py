import json
import os


def serialize_collection(collection_dict: dict) -> None:
    if list(collection_dict.keys()) != ['id', 'title', 'cards']:
        raise ValueError
    filename = f'collections/{collection_dict["id"]}//{collection_dict["id"]}.json'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w+', encoding='utf-8') as f:
        json.dump(collection_dict, f, ensure_ascii=False, indent=4)
