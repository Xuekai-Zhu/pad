def solution():
    """In four years, Peter will be twice as old as Harriet. If Peter's age is currently half of his mother's age, who is 60, how old is Harriet now?"""
    # Define the current age of Peter's mother
    mother_age = 60

    # Calculate Peter's current age
    peter_age = mother_age / 2

    # Calculate Harriet's current age
    harriet_age = (peter_age * 2) - 4

    result = harriet_age
    return result

print(solution())