def solution():
    # Define the prices of each item
    tshirt_price = 5
    pants_price = 4
    skirt_price = 6
    refurbished_price = tshirt_price / 2

    # Define the number of each item sold
    num_tshirts = 2
    num_pants = 1
    num_skirts = 4
    num_refurbished = 6

    # Calculate the total income
    total_income = (tshirt_price * num_tshirts) + (pants_price * num_pants) + \
                   (skirt_price * num_skirts) + (refurbished_price * num_refurbished)

    result = total_income
    return result

print(solution())