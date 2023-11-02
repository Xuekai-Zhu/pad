def solution():
    """Emmanuel will stay in Guam in December for 10 days in which he has to use international data that would cost $3.50 per day. Emmanuel has been paying $175 per month for his regular plan. How much in all will be Emmanuel’s charges for December?"""
    # Define the cost of international data per day and regular plan cost per month
    INTERNATIONAL_DATA_COST = 3.5
    REGULAR_PLAN_COST = 175

    # Calculate the cost of international data for 10 days
    international_data_cost = 10 * INTERNATIONAL_DATA_COST

    # Calculate the total cost for December
    total_cost = international_data_cost + REGULAR_PLAN_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())