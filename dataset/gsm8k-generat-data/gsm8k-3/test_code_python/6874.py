def solution():
    """Mandy’s phone data plan charges $30 per month for data. Her first month, she got a promotional rate of one-third the normal price. However, in the fourth month she went over her data limit and was charged an extra fee of $15. How much did Mandy pay in the first 6 months for data?"""
    # Define the regular monthly cost and the promotional rate
    REGULAR_COST = 30
    PROMOTIONAL_RATE = 1/3

    # Calculate the cost of Mandy's first month with the promotional rate
    first_month_cost = REGULAR_COST * PROMOTIONAL_RATE

    # Calculate the total cost of Mandy's data plan for the first 6 months
    total_cost = (first_month_cost * 1) + (REGULAR_COST * 3) + (REGULAR_COST + 15) + (REGULAR_COST * 1)

    # Display the total cost
    result = total_cost
    return result

print(solution())