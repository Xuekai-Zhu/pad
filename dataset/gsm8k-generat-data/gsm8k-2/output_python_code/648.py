def solution():
    """Some students want to buy pencils from a stationery shop. The price of one pencil is 20 cents. Tolu wants 3 pencils, Robert wants 5 pencils and Melissa wants 2 pencils. How much (in dollars) will the students spend altogether at the stationery shop?"""
    pencil_price = 0.2
    tolu_pencils = 3
    robert_pencils = 5
    melissa_pencils = 2
    total_pencils = tolu_pencils + robert_pencils + melissa_pencils
    total_price = total_pencils * pencil_price
    result = total_price
    return result

print(solution())