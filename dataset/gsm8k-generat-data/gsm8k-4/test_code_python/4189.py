def solution():
    """In eight years, Mr. Bernard will be 3 times as old as Luke is now. If Luke is 20, what is 10 years less than their average age?"""
    # Define Luke's current age
    luke_age = 20

    # Calculate Mr. Bernard's age in 8 years
    bernard_age_plus_8 = luke_age * 3

    # Calculate Mr. Bernard's current age
    bernard_age = bernard_age_plus_8 - 8

    # Calculate the average age of Luke and Mr. Bernard
    average_age = (luke_age + bernard_age) / 2

    # Calculate 10 years less than their average age
    result = average_age - 10
    return result

print(solution())