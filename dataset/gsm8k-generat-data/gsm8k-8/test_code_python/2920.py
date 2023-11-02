def solution():
    # Define the ages of Molly and Jared
    molly_age = 30
    jared_age = molly_age + 10

    # Calculate the total age of the three friends
    total_age = 40 * 3

    # Calculate Hakimi's age
    hakimi_age = total_age - (molly_age + jared_age)

    result = hakimi_age
    return result

print(solution())