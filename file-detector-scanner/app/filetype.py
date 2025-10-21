def identify_by_magic(path: str):
    # Read file header
    with open(path, "rb") as f:
        header = f.read(16)

    # Binary file signatures
    if header.startswith(b"MZ"):
        return "pe (Windows Executable)"
    if header.startswith(b"\xFF\xD8\xFF"):
        return "jpeg image"
    if header.startswith(b"%PDF-"):
        return "pdf document"

    # Check for text file
    try:
        with open(path, "r", encoding="utf-8") as f:
            f.read()  # Try reading as text
        return "text file"
    except:
        pass

    # Unknown file type
    return "unknown"



