def solution():
    """Victor works at Clucks Delux, a restaurant specializing in chicken. An order of Chicken Pasta uses 2 pieces of chicken, an order of Barbecue Chicken uses 3 pieces of chicken, and a family-size Fried Chicken Dinner uses 8 pieces of chicken. Tonight, Victor has 2 Fried Chicken Dinner orders, 6 Chicken Pasta orders, and 3 Barbecue Chicken orders. How many pieces of chicken does he need for all the orders?"""
    chicken_pasta = 6 * 2
    barbecue_chicken = 3 * 3
    fried_chicken = 2 * 8
    total_chicken = chicken_pasta + barbecue_chicken + fried_chicken
    result = total_chicken
    return result

print(solution())