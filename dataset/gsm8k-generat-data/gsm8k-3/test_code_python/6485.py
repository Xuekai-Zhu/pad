def solution():
    """My age is five times that of my son. Next year, my son will be eight years old. How old am I now?"""
    # Define the age of the son next year
    son_next_year = 8

    # Calculate the age of the son now
    son_now = son_next_year - 1

    # Calculate my age
    my_age = son_now * 5

    # Display my age
    result = my_age
    return result

print(solution())