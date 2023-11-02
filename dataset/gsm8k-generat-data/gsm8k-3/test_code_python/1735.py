def solution():
    """Karl sells clothing in his store. He sells a T-shirt that costs $5, some pants that cost $4, and some skirts that cost $6, he also sells some refurbished t-shirts that cost half the original price. How much is his total income if he sold two T-shirts, one pair of pants, four skirts, and six refurbished T-shirts?"""
    # Define the prices of each item
    TSHIRT_PRICE = 5
    PANTS_PRICE = 4
    SKIRT_PRICE = 6
    REFURBISHED_TSHIRT_PRICE = TSHIRT_PRICE / 2

    # Define the number of each item sold
    tshirts_sold = 2
    pants_sold = 1
    skirts_sold = 4
    refurbished_tshirts_sold = 6

    # Calculate the income from each type of item sold
    tshirt_income = tshirts_sold * TSHIRT_PRICE
    pants_income = pants_sold * PANTS_PRICE
    skirts_income = skirts_sold * SKIRT_PRICE
    refurbished_tshirt_income = refurbished_tshirts_sold * REFURBISHED_TSHIRT_PRICE

    # Calculate the total income
    total_income = tshirt_income + pants_income + skirts_income + refurbished_tshirt_income

    # Display the total income
    result = total_income
    return result

print(solution())