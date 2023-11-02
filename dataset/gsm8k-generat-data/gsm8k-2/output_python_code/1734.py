def solution():
    """Karl sells clothing in his store. He sells a T-shirt that costs $5, some pants that cost $4, and some skirts that cost $6, he also sells some refurbished t-shirts that cost half the original price. How much is his total income if he sold two T-shirts, one pair of pants, four skirts, and six refurbished T-shirts?"""
    tshirt_price = 5
    pants_price = 4
    skirt_price = 6
    refurbished_price = tshirt_price / 2
    total_income = (2*tshirt_price) + pants_price + (4*skirt_price) + (6*refurbished_price)
    result = total_income
    return result

print(solution())