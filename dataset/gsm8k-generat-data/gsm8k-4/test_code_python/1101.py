def solution():
    """Beckett is 12 and is three years younger than Olaf, while Shannen is two years younger than Olaf. If Jack is five more than twice as old as Shannen, what is the sum of the ages of all 4 people?"""
    # Define the age of Beckett
    beckett_age = 12

    # Calculate the age of Olaf
    olaf_age = beckett_age + 3

    # Calculate the age of Shannen
    shannen_age = olaf_age - 2

    # Calculate the age of Jack
    jack_age = 5 + 2 * shannen_age

    # Calculate the sum of the ages of all 4 people
    total_age = beckett_age + olaf_age + shannen_age + jack_age

    # return the result
    result = total_age
    return result

print(solution())