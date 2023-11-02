def solution():
    """Alexis is applying for a new job and bought a new set of business clothes to wear to the interview. She went to a department store with a budget of $200 and spent $30 on a button-up shirt, $46 on suit pants, $38 on a suit coat, $11 on socks, and $18 on a belt. She also purchased a pair of shoes, but lost the receipt for them. She has $16 left from her budget. How much did Alexis pay for the shoes?"""
    # Define the total budget and the prices of the clothes
    total_budget = 200
    shirt_price = 30
    pants_price = 46
    coat_price = 38
    socks_price = 11
    belt_price = 18

    # Calculate the total cost of the clothes
    total_clothes_cost = shirt_price + pants_price + coat_price + socks_price + belt_price

    # Calculate the amount spent on the shoes
    shoes_price = total_budget - total_clothes_cost - 16

    result = shoes_price
    return result

print(solution())