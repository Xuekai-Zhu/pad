def solution():
    num_shirts = 5
    shirt_price = 1

    num_pants = 5
    pants_price = 3

    # Calculate the total money earned from selling shirts
    shirt_total = num_shirts * shirt_price

    # Calculate the total money earned from selling pants
    pants_total = num_pants * pants_price

    # Calculate the total money earned from selling all clothes
    total_earned = shirt_total + pants_total

    # Calculate Kekai's share of the money after giving half to his parents
    kekai_money = total_earned / 2

    result = kekai_money
    return result

print(solution())