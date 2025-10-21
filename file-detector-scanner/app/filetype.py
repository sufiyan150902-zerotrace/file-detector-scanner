def identify_by_magic(path: str):
    with open(path, "rb") as f:
        header = f.read(16)
    if header.startswith(b"MZ"):
        return "pe (Windows Executable)"
    if header.startswith(b"\xFF\xD8\xFF"):
        return "jpeg image"
    if header.startswith(b"%PDF-"):
        return "pdf document"
    return "unknown"

