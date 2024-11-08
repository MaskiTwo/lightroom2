from dotenv import load_dotenv
import os

def main():
    print(f"hello world {os.getenv('key')}")

if __name__ == "__main__":
    load_dotenv()
    main()