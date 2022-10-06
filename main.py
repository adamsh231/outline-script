# import OS module
from helper import *
import os
import argparse

# Project name
parser = argparse.ArgumentParser()
parser.add_argument("--name", help="Knowledge center name of this project", default=False)
project_name = parser.parse_args().name
if not project_name:
    raise ValueError("--name 'Name of this Project' is Required in args")

# Project automation
project_path = os.path.normpath(os.getcwd() + os.sep + os.pardir) + "/"
readme_content = get_content_from_file(project_path + README_FILE_NAME)
data = searchDocs(project_name)
project_id = ""
if len(data) == 0:
    project_id = createDocs(project_name, None, readme_content)
else:
    project_id = data[0]["document"]["id"]
    updateDocs(project_id, project_name, readme_content)

# Documentation file walk
docs_name = "docs"
docs_path = project_path + docs_name + "/"
doc_list = []
for root, dirs, files in os.walk(docs_path, topdown=True):
    for name in files:
        
        # Extension validation
        file_detail = os.path.splitext(name)
        if file_detail[1].lower() != ALLOWED_FILE_EXT.lower() and file_detail[1].lower() != "":
            continue
        
        # Save file walk
        file_name = os.path.join(root, name)
        arr_file = file_name.replace(docs_path, "").split("/") # todo: windows -> \\
        arr_file.insert(0, docs_name)
        doc_list.append(arr_file)

# Documentation file walk automation
for index, file in enumerate(doc_list):
    parent_id, parent_name = project_id, project_name
    path = project_path
    for idx, val in enumerate(file):
        
        # Modification path
        path += val
        content = get_content_from_file(path)

        # Validation and modification title extension
        is_readme_file = val.lower() == README_FILE_NAME.lower()
        file_detail = os.path.splitext(name)
        if file_detail[1].lower() != "":
            val = val.lower().replace(ALLOWED_FILE_EXT, "")

        # Modification space underscore
        val = val.replace("_", " ").title()

        # Folder
        if idx < len(file) - 1:
            path += "/"
            # val = "Documentation" if val == "Docs" else val # Modification Docs
            is_exist, parent_id = documentParentMapping(parent_id, val, searchDocs(val))
            if not is_exist:
                parent_id = createDocs(val, parent_id, content)
                
        # File
        else:
            
            # Readme
            if is_readme_file:
                updateDocs(parent_id, parent_name, content)
                
            # Other
            else:
                is_exist, parent_id = documentParentMapping(parent_id, val, searchDocs(val))
                if is_exist:
                    updateDocs(parent_id, val, content)
                else:
                    parent_id = createDocs(val, parent_id, content)
                    
        parent_name = val
        

