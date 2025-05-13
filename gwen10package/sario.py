from pyjokes import get_joke

def tell_joke():
    """
    Print a programming joke using the pyjokes module.
    """
    print("\n-------------------------------------------------------")
    print(f"\nJoke of the day: {get_joke()}")