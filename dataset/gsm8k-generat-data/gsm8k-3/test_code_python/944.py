def solution():
    """Kylie has 5 daisies. Her sister gave her another 9 daisies. Kylie then gave half her daisies to her mother. How many daisies does Kylie have left?"""
    # Define the initial number of daisies Kylie had
    initial_daisies = 5

    # Define the number of daisies Kylie's sister gave her
    sister_daisies = 9

    # Calculate the total number of daisies Kylie has
    total_daisies = initial_daisies + sister_daisies

    # Calculate the number of daisies Kylie gave to her mother
    mother_daisies = total_daisies // 2

    # Calculate the number of daisies Kylie has left
    remaining_daisies = total_daisies - mother_daisies

    # Display the number of daisies Kylie has left
    result = remaining_daisies
    return result

print(solution())