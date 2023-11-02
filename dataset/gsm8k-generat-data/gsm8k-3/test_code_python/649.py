def solution():
    """Some students want to buy pencils from a stationery shop. The price of one pencil is 20 cents. Tolu wants 3 pencils, Robert wants 5 pencils and Melissa wants 2 pencils. How much (in dollars) will the students spend altogether at the stationery shop?"""
    # Define the price of one pencil in cents and the number of pencils each student wants
    PENCIL_PRICE = 20
    tolus_pencils = 3
    roberts_pencils = 5
    melissas_pencils = 2

    # Calculate the total cost of all the pencils
    total_cost = (tolus_pencils + roberts_pencils + melissas_pencils) * PENCIL_PRICE / 100

    # Display the total cost in dollars
    result = total_cost
    return result

print(solution())