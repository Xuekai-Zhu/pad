def solution():
    """Janet has 24 dresses. Half of them have pockets. Of those, a third have 2 pockets and the rest have 3 pockets. How many total pockets do her dresses have?"""
    # Define the number of dresses and calculate the number of dresses with pockets
    total_dresses = 24
    pocketed_dresses = total_dresses // 2

    # Calculate the number of dresses with 2 pockets and 3 pockets
    dresses_with_2_pockets = pocketed_dresses // 3
    dresses_with_3_pockets = pocketed_dresses - dresses_with_2_pockets

    # Calculate the total number of pockets
    total_pockets = (dresses_with_2_pockets * 2) + (dresses_with_3_pockets * 3)

    result = total_pockets
    return result

print(solution())