import os

def file_names():
    cwd = os.getcwd()
    dir_list = os.listdir(cwd)
    return dir_list


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names