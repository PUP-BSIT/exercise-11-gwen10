import requests

def check_internet():
    """
    Checks if the device has an active internet connection 
    by attempting to reach Google.
    """
    print("\n-------------------------------------------------------")
    print("\nWelcome To Internet Checker.")
    print("\nChecking internet connection...")
    try:
        requests.get("https://www.google.com", timeout=5)
        print("\nYour internet connection is active.")
    except requests.ConnectionError:
        print("\nYour internet connection is not active.")
