def solution():
    # Calculate the total income from selling clothing
    tshirt_income = 5 * 2  # sold 2 T-shirts for $5 each
    pants_income = 4 * 1  # sold 1 pair of pants for $4
    skirts_income = 6 * 4  # sold 4 skirts for $6 each
    refurbished_income = (5/2) * 6  # sold 6 refurbished T-shirts for half the original price

    total_income = tshirt_income + pants_income + skirts_income + refurbished_income
    result = total_income
    return result

print(solution())