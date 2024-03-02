#Title: "UUID Generator""
#Description: "This program generates a UUID and validates a UUID entered by the user."
#Author: "JonesCKevin"
#Date: "01 Mar 2024"

import uuid                                                             # Import the UUID module

def generate_uuid():                                                    # Function to generate a UUID
    return str(uuid.uuid4())                                            # Return the generated UUID

def validate_uuid(uuid_str):                                            # Function to validate a UUID
    try:                                                                # Try to validate the UUID
        uuid.UUID(uuid_str)                                             # Validate the UUID
        return True                                                     # Return True if the UUID is valid
    except ValueError:                                                  # If the UUID is invalid
        return False                                                    # Return False if the UUID is invalid

new_uuid = generate_uuid()                                             # Generate a new UUID
print(f"\nGenerated UUID:")
print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")                              
for _ in range(10):                                                     # Replays def generate_uuid 10 times
        print(generate_uuid())                                          
print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
user_input = input("Enter a UUID to validate: ")                        # Ask the user to enter a UUID
if validate_uuid(user_input):                                           # Validate the UUID
    print()                                                             # Add a newline here
    print(f"The UUID You have provided is a Valid UUID: {user_input}")  # Print the valid UUID
    print()                                                             # Add a newline here
else:                                                                   # If the UUID is invalid
    print()                                                             # Add a newline here
    print("You have provided an Invalid UUID")                          # Print the invalid UUID
    print()                                                             # Add a newline here
