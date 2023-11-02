def solution():
    cherry_price = 8  # Cherries cost $8 per kilogram
    total_price = 1600  # Genevieve had $1600
    amount_short = 400  # Genevieve was $400 short of the total price
    total_weight = (total_price - amount_short) / cherry_price  # Calculate the total weight of cherry bought

    result = total_weight
    return result

print(solution())