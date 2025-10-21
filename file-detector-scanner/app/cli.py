import argparse
from .scanner import scan_path

def main():
    parser = argparse.ArgumentParser(description="Simple File Identifier & Hash Scanner")
    parser.add_argument("target", help="Path to file you want to scan")
    args = parser.parse_args()

    result = scan_path(args.target)
    print(result)

if __name__ == "__main__":
    main()

