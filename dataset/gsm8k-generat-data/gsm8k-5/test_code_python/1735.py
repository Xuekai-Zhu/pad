def solution():
    tshirt_price = 5
    pants_price = 4
    skirts_price = 6
    refurbished_tshirt_price = tshirt_price / 2

    # Calculate the total income from selling 2 T-shirts, 1 pair of pants, 4 skirts, and 6 refurbished T-shirts
    total_income = (2 * tshirt_price) + (1 * pants_price) + (4 * skirts_price) + (6 * refurbished_tshirt_price)
    result = total_income
    return result

print(solution())