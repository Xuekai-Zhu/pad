def solution():
    
    # Define the combined age of Peter and Jean
    combined_age = 100

    # Calculate Paul's age
    paul_age = combined_age - 10

    # Calculate John's age
    john_age = paul_age + 10

    # Calculate Peter's age
    peter_age = paul_age + john_age

    # Display Peter's age
    result = peter_age
    return result

print(solution())