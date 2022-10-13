import requests
import argparse

# Initial constant
KNOWLEDGE_CENTER_ENDPOINT = "https://outline.rnd.mangkujagat.com/api"
README_FILE_NAME = "Readme.MD"
ALLOWED_FILE_EXT = ".md"

# Command
parser = argparse.ArgumentParser()
parser.add_argument("--name", help="Knowledge center name of this project", default=False)
parser.add_argument("--token", help="Outline api token", default=False)
parser.add_argument("--cid", help="Collection ID", default=False)

# Project name
project_name = parser.parse_args().name
if not project_name:
    raise ValueError("--name 'Name of this Project' is Required in args")

# Token
project_token = parser.parse_args().token
if not project_token:
    raise ValueError("--token 'Outline api token' is Required in args")

collection_id = parser.parse_args().cid
if not collection_id:
    raise ValueError("--cid 'Collection ID")

def get_content_from_file(file_path):
    content = ""
    try:
        content = open(file_path).read()
    except:
        content = ""
    return content


def send_request_to_outline(url, payload):
    headers = {
        "content-type": "application/json",
        "Authorization": "Bearer " + project_token,
    }
    r = requests.post(KNOWLEDGE_CENTER_ENDPOINT + url, json=payload, headers=headers)
    if r.status_code != requests.codes.ok:
        print(r.json())
        raise ValueError(r.raise_for_status())
    return r


def searchDocs(query):
    r = send_request_to_outline(
        "/documents.search",
        {
            "query": query,
            "collectionId": collection_id,
            "includeArchived": False,
            "includeDrafts": False,
        },
    )
    return r.json()["data"]


def createDocs(title, parent_id, content):
    r = send_request_to_outline(
        "/documents.create",
        payload={
            "title": title,
            "collectionId": collection_id,
            "parentDocumentId": parent_id,
            "text": content,
            "publish": True,
        },
    )
    print(title + " Created")
    return r.json()["data"]["id"]


def updateDocs(id, title, content):
    r = send_request_to_outline(
        "/documents.update",
        payload={
            "id": id,
            "title": title,
            "text": content,
            "append": False,
            "publish": True,
            "done": True,
        },
    )
    print(title + " Updated")


def documentParentMapping(parent_id, title, data):
    for val in data:
        if val["document"]["parentDocumentId"] == parent_id and val["document"]["title"] == title:
            return True, val["document"]["id"]
    return False, parent_id
