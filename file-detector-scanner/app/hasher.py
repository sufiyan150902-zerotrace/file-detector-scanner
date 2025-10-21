import hashlib

def compute_hashes(path: str):
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    with open(path, "rb") as f:
        data = f.read()
        md5.update(data)
        sha1.update(data)
        sha256.update(data)
    return {
        "md5": md5.hexdigest(),
        "sha1": sha1.hexdigest(),
        "sha256": sha256.hexdigest()
    }
