from .hasher import compute_hashes
from .filetype import identify_by_magic

def scan_path(path: str):
    return {
        "file": path,
        "hashes": compute_hashes(path),
        "file_type": identify_by_magic(path)
    }

