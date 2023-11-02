def solution():
    """John is half times younger than his father, who is 4 years older than John's mother. If John's father is 40 years old, what's the age difference between John and his mother?"""
    # Calculate John's father's age since we know John's father is 40 years old
    father_age = 40

    # Calculate John's mother's age
    mother_age = father_age - 4

    # Calculate John's age since we know John is half times younger than his father
    john_age = 0.5*father_age

    # Calculate the age difference between John and his mother
    difference = mother_age - john_age

    # Display the age difference
    result = difference
    return result

print(solution())