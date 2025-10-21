# app/filetype.py

# Dictionary of common file signatures (magic bytes)
FILE_SIGNATURES = {
    b'\xFF\xD8\xFF': 'JPEG',
    b'\x89PNG\r\n\x1A\n': 'PNG',
    b'%PDF-': 'PDF',
    b'MZ': 'PE',  # Windows executable
    # You can add more signatures here
}

def identify_file_type(file_path):
    """
    Identify the type of a file based on its header (magic bytes).
    Returns 'TXT' if it's a readable text file, or 'unknown'.
    """
    try:
        with open(file_path, 'rb') as f:
            header = f.read(8)  # Read first 8 bytes
    except Exception as e:
        return f"Error reading file: {e}"

    # 1️⃣ Check known binary signatures
    for sig, ftype in FILE_SIGNATURES.items():
        if header.startswith(sig):
            return ftype

    # 2️⃣ Check for text file
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            f.read()
        return 'TXT'
    except:
        pass

    # 3️⃣ If nothing matches
    return 'unknown'

# Optional: quick test when running file directly
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        print(f"{file_path}: {identify_file_type(file_path)}")
    else:
        print("Usage: python filetype.py <file_path>")


