def classify_file(filename):
    if filename.endswith(".pdf"):
        return "Documento"

    if filename.endswith(".jpg"):
        return "Imagem"

    return "Outro"
