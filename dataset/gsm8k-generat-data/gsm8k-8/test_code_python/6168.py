def solution():
    # Define the initial number of apples and oranges
    initial_apples = 50
    initial_oranges = 40

    # Define the prices of an apple and an orange
    apple_price = 0.80
    orange_price = 0.50

    # Calculate the total revenue earned from the apples and oranges sold
    revenue_from_apples = (initial_apples - 10) * apple_price
    revenue_from_oranges = (initial_oranges - 6) * orange_price
    total_revenue = revenue_from_apples + revenue_from_oranges

    result = total_revenue
    return result

print(solution())