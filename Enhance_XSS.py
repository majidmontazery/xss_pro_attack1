import requests
from urllib.parse import urlparse

def load_payloads():
    """Load multiple XSS payloads from user input or a file."""
    payloads = []
    
    while True:
        choice = input("\nEnter payloads manually or load from file? (manual/file): ").strip().lower()
        
        if choice == "file":
            file_path = input("\nEnter payload file path (e.g., payloads.txt): ").strip()
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    payloads = [line.strip() for line in file if line.strip()]
                print(f"\n Loaded {len(payloads)} payloads from {file_path}\n")
                return payloads  # Return after successful load
            except FileNotFoundError:
                print("\n Error: File not found. Please enter a valid file path.")
            except Exception as e:
                print(f"\n Error reading file: {e}")
        
        elif choice == "manual":
            print("\nEnter XSS payloads (Type 'done' to finish):")
            while True:
                payload = input(f"{len(payloads) + 1}. ").strip()  # Numbered input
                if payload.lower() == "done":
                    return payloads  # Return collected payloads
                payloads.append(payload)
        
        else:
            print("\n Invalid option. Please enter 'manual' or 'file'.")

def main():
    print("\n XSS Vulnerability Scanner")

    url = input("\nEnter the target URL (e.g., https://example.com/search): ").strip()
    
    parsed_url = urlparse(url)
    if not parsed_url.scheme or not parsed_url.netloc:
        print(" Invalid URL. Please enter a valid URL (e.g., https://example.com).")
        return

    param = input("Enter the vulnerable parameter name (e.g., 'q' for ?q=search): ").strip()

    payloads = load_payloads()
    
    if not payloads:
        print("\n No payloads provided. Exiting.")
        return

    print("\n Starting XSS Tests...\n")

if __name__ == "__main__":
    main()
