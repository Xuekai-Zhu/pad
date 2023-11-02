def solution():
    # Define the price and quantity of each type of ticket
    matinee_price = 5
    matinee_quantity = 200
    evening_price = 12
    evening_quantity = 300
    three_d_price = 20
    three_d_quantity = 100

    # Calculate the total revenue from each type of ticket
    matinee_revenue = matinee_price * matinee_quantity
    evening_revenue = evening_price * evening_quantity
    three_d_revenue = three_d_price * three_d_quantity

    # Calculate the total revenue
    total_revenue = matinee_revenue + evening_revenue + three_d_revenue
    result = total_revenue
    return result

print(solution())