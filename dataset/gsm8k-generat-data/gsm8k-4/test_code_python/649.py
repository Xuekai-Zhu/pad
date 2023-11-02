def solution():
    """Some students want to buy pencils from a stationery shop. The price of one pencil is 20 cents. Tolu wants 3 pencils, Robert wants 5 pencils and Melissa wants 2 pencils. How much (in dollars) will the students spend altogether at the stationery shop?"""
    # Define the price of one pencil and the number of pencils each student wants
    pencil_price_cents = 20
    tolu_pencils = 3
    robert_pencils = 5
    melissa_pencils = 2

    # Calculate the total cost of all the pencils
    total_cost_cents = (tolu_pencils + robert_pencils + melissa_pencils) * pencil_price_cents

    # Convert the total cost to dollars
    total_cost_dollars = total_cost_cents / 100

    # return the result
    result = total_cost_dollars
    return result

print(solution())