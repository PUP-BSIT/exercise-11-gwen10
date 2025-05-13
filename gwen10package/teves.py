from faker import Faker

def fake_profile():
    """Generate and display a fake user profile with name, 
    username, and email."""
    
    fake = Faker()
    
    print("\n-------------------------------------------------------")
    print(" ")
    print("Hello, welcome to the profile generator!")
    print("\nHere's your generated profile:\n")

    print("Name:", fake.name())
    print("Username:", fake.user_name())
    print("Email:", fake.email())