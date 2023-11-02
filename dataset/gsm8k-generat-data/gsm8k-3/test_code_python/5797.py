def solution():
    """At a coffee shop, 7 customers order coffee at $5 each and 8 customers order tea at $4 each. How much money did the coffee shop make?"""
    # Define the cost of coffee and tea
    COFFEE_COST = 5
    TEA_COST = 4

    # Define the number of customers that ordered coffee and tea
    coffee_customers = 7
    tea_customers = 8

    # Calculate the total amount of money made from coffee and tea
    coffee_sales = coffee_customers * COFFEE_COST
    tea_sales = tea_customers * TEA_COST
    total_sales = coffee_sales + tea_sales

    # Display the total amount of money made
    result = total_sales
    return result

print(solution())