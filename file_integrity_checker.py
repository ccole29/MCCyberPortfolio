import hashlib

def calculate_sha256(file_path):
    """Calculate the SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"[Error] File not found: {file_path}")
    except PermissionError:
        print(f"[Error] Permission denied: {file_path}")
    return None

if __name__ == "__main__":
    path = input("Enter the path to the file: ").strip()
    hash_result = calculate_sha256(path)
    if hash_result:
        print(f"\nSHA256 Hash:\n{hash_result}")
