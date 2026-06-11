from pathlib import Path

def scan_folder(folder):
    files = []

    for item in Path(folder).rglob("*"):
        if item.is_file():
            files.append(item)

    return files
