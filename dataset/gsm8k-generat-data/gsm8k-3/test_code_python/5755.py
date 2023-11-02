def solution():
    """John is twice as old as Mary and half as old as Tonya. If Tanya is 60, what is their average age?"""
    # Define Tonya's age and calculate John's and Mary's ages
    tanya_age = 60
    john_age = tanya_age / 2
    mary_age = john_age / 2

    # Calculate the average age
    average_age = (john_age + mary_age + tanya_age) / 3

    # Display the average age
    result = average_age
    return result

print(solution())