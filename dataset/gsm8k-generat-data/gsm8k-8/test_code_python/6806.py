def solution():
    # Define the original price and the number of dolls Daniel can buy with his savings
    original_price = 4
    num_dolls = 15

    # Calculate the total cost of the dolls at the original price
    total_cost = original_price * num_dolls

    # Calculate the new price per doll and the number of dolls Daniel can buy at the discounted price
    new_price = 3
    num_discounted_dolls = total_cost / new_price

    result = num_discounted_dolls
    return result

print(solution())