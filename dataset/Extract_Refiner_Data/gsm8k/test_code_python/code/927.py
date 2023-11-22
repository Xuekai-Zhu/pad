def solution():
    
    # Define the combined age of Peter, Paul, and Jean
    combined_age = 100

    # Calculate the age of John
    john_age = combined_age - 10

    # Calculate the age of Paul
    paul_age = john_age + 10

    # Calculate the sum of Paul and John's age
    paul_and_john_age = paul_age + john_age

    # Calculate Peter's age
    peter_age = paul_and_john_age

    # Display Peter's age
    result = peter_age
    return result

print(solution())