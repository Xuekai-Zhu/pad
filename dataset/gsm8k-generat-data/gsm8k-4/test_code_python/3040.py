def solution():
    """Tim is 5 years old. His cousin, Rommel, is thrice as old as he is. His other cousin, Jenny, is 2 years older than Rommel. How many years younger is Tim than Jenny?"""
    # Define Tim's age
    tim_age = 5

    # Calculate Rommel's age
    rommel_age = tim_age * 3

    # Calculate Jenny's age
    jenny_age = rommel_age + 2

    # Calculate the age difference between Tim and Jenny
    age_difference = jenny_age - tim_age

    # Return the result
    result = age_difference
    return result

print(solution())