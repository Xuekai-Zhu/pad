def solution():
    retail_price = 600  # The retail price of the bike is $600
    saved_amount = 120  # Maria has saved $120 for the purchase
    mother_contribution = 250  # Maria's mother will contribute $250 towards the purchase

    # Calculate the remaining amount Maria needs to purchase the bike
    remaining_amount = retail_price - saved_amount - mother_contribution

    result = remaining_amount
    return result

print(solution())