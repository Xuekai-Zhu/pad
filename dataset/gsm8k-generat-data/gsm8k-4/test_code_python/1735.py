def solution():
    """Karl sells clothing in his store. He sells a T-shirt that costs $5, some pants that cost $4, and some skirts that cost $6, he also sells some refurbished t-shirts that cost half the original price. How much is his total income if he sold two T-shirts, one pair of pants, four skirts, and six refurbished T-shirts?"""
    # Define the prices of the items
    tshirt_price = 5
    pants_price = 4
    skirt_price = 6

    # Calculate the total income from selling regular T-shirts and pants
    regular_income = (2 * tshirt_price) + pants_price

    # Calculate the total income from selling skirts
    skirt_income = 4 * skirt_price

    # Calculate the total income from selling refurbished T-shirts
    refurbished_income = (6 * tshirt_price) / 2

    # Calculate the total income from all sales
    total_income = regular_income + skirt_income + refurbished_income

    result = total_income
    return result

print(solution())