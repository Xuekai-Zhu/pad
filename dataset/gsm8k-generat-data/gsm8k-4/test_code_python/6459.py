def solution():
    """Juliet is 3 years older than her sister Maggie but 2 years younger than her elder brother Ralph. If Juliet is 10 years old, what is the sum of Maggie's and Ralph's ages?"""
    # Define Juliet's age and the age difference between her and Maggie
    juliet_age = 10
    maggie_age_difference = 3

    # Calculate Maggie's age
    maggie_age = juliet_age - maggie_age_difference

    # Calculate Ralph's age
    ralph_age = juliet_age + 2

    # Calculate the sum of Maggie's and Ralph's ages
    total_age = maggie_age + ralph_age

    # return the result
    result = total_age
    return result

print(solution())