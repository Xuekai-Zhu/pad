def solution():
    """Beckett is 12 and is three years younger than Olaf, while Shannen is two years younger than Olaf.  If Jack is five more than twice as old as Shannen, what is the sum of the ages of all 4 people?"""
    # Define Beckett's age
    beckett = 12

    # Calculate Olaf's age
    olaf = beckett + 3

    # Calculate Shannen's age
    shannen = olaf - 2

    # Calculate Jack's age
    jack = 2 * shannen + 5

    # Calculate the sum of all four people's ages
    total_age = beckett + olaf + shannen + jack

    # Display the sum of all four people's ages
    result = total_age
    return result

print(solution())