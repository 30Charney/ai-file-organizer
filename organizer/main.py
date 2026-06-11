from organizer.scanner import scan_folder

folder = input("Digite o caminho da pasta: ")

files = scan_folder(folder)

print(f"Encontrados {len(files)} arquivos")
