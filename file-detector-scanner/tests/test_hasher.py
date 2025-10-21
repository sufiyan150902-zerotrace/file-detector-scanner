import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.hasher import compute_hashes
import os, tempfile

def test_hash_lengths():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b"abc")
        path = f.name
    try:
        h = compute_hashes(path)
        assert len(h["md5"]) == 32
        assert len(h["sha1"]) == 40
        assert len(h["sha256"]) == 64
    finally:
        os.remove(path)

