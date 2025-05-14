from mimesis import Person

def random_person_info():
    """
    Generate and display random personal information.

    This function uses the Mimesis library to generate a random person's
    full name, and email address, and prints them to the console.
    """
    print("\n-------------------------------------------------------")
    print(" ")
    print("Hello, welcome to the random person info generator!")
    print("\nTa-da! Here's the profile we made for you:\n")

    person = Person()
    print("Full name: ", person.full_name())
    print("Email: ", person.email()) 
    print("\n-------------------------------------------------------")