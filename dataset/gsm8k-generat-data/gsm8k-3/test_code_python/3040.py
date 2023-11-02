def solution():
    """Tim is 5 years old. His cousin, Rommel, is thrice as old as he is. His other cousin, Jenny, is 2 years older than Rommel. How many years younger is Tim than Jenny?"""
    # Define Tim's age and calculate Rommel and Jenny's ages
    tim_age = 5
    rommel_age = 3 * tim_age
    jenny_age = rommel_age + 2

    # Calculate the age difference between Tim and Jenny
    age_difference = jenny_age - tim_age

    # Display the age difference
    result = age_difference
    return result

print(solution())