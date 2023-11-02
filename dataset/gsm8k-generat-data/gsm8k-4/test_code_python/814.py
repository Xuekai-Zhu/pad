def solution():
    """Every Sunday, Sean picks up 1 almond croissant and 1 salami and cheese croissant that are $4.50 each. He also grabs a plain croissant for $3.00 and a loaf of focaccia for $4.00. On his way home, he stops and picks up 2 lattes for $2.50 each. How much did he spend?"""
    # Define the prices of each item
    almond_croissant = 4.5
    salami_cheese_croissant = 4.5
    plain_croissant = 3.0
    focaccia = 4.0
    latte = 2.5

    # Calculate the total cost of Sean's purchases
    total_cost = (almond_croissant + salami_cheese_croissant + plain_croissant +
                  focaccia + (2 * latte))

    # Return the result
    result = total_cost
    return result

print(solution())