import requests

# Initial constant
KNOWLEDGE_CENTER_TOKEN = "XnWPxNjmUJ2Ukzf22zrCGOCyfx9mvkmrTTMyp1"
KNOWLEDGE_CENTER_ENDPOINT = "https://outline.rnd.mangkujagat.com/api"
COLLECTION_ID = "e8e53145-445a-417c-ac61-bb52e23af200"
README_FILE_NAME = "Readme.MD"
ALLOWED_FILE_EXT = ".md"


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
        "Authorization": "Bearer " + KNOWLEDGE_CENTER_TOKEN,
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
            "collectionId": COLLECTION_ID,
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
            "collectionId": COLLECTION_ID,
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