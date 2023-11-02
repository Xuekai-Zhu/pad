def solution():
    num_tshirts = 2
    tshirt_price = 5

    num_pants = 1
    pants_price = 4

    num_skirts = 4
    skirt_price = 6

    num_refurbished_tshirts = 6
    refurbished_tshirt_price = tshirt_price / 2

    # Calculate the total income from selling t-shirts
    total_tshirt_income = num_tshirts * tshirt_price

    # Calculate the total income from selling pants
    total_pants_income = num_pants * pants_price

    # Calculate the total income from selling skirts
    total_skirts_income = num_skirts * skirt_price

    # Calculate the total income from selling refurbished t-shirts
    total_refurbished_tshirt_income = num_refurbished_tshirts * refurbished_tshirt_price

    # Calculate the total income from selling all items
    total_income = total_tshirt_income + total_pants_income + total_skirts_income + total_refurbished_tshirt_income
    result = total_income
    return result

print(solution())