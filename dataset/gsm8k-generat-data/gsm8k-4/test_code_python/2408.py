def solution():
    """Emmanuel will stay in Guam in December for 10 days in which he has to use international data that would cost $3.50 per day. Emmanuel has been paying $175 per month for his regular plan. How much in all will be Emmanuel’s charges for December?"""
    # Define the cost of international data and regular plan
    international_data_cost = 3.5
    regular_plan_cost = 175

    # Calculate the cost of regular plan per day
    regular_plan_cost_per_day = regular_plan_cost / 30

    # Calculate the total cost for 10 days with international data
    total_cost = (regular_plan_cost_per_day + international_data_cost) * 10

    result = total_cost
    return result

print(solution())