def solution():
    # Calculate the total number of pieces of chicken needed for Chicken Pasta orders
    chicken_pasta = 6 * 2  # 6 orders times 2 pieces of chicken per order

    # Calculate the total number of pieces of chicken needed for Barbecue Chicken orders
    barbecue_chicken = 3 * 3  # 3 orders times 3 pieces of chicken per order

    # Calculate the total number of pieces of chicken needed for Fried Chicken Dinner orders
    fried_chicken_dinner = 2 * 8  # 2 orders times 8 pieces of chicken per order

    # Calculate the total number of pieces of chicken needed for all the orders
    total_chicken = chicken_pasta + barbecue_chicken + fried_chicken_dinner
    result = total_chicken
    return result

print(solution())