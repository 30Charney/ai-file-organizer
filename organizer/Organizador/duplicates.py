import hashlib

def get_file_hash(filepath):
    hasher = hashlib.md5()

    with open(filepath, "rb") as file:
        while chunk := file.read(4096):
            hasher.update(chunk)

    return hasher.hexdigest()
