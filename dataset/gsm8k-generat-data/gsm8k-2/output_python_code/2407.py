def solution():
    """Emmanuel will stay in Guam in December for 10 days in which he has to use international data that would cost $3.50 per day. Emmanuel has been paying $175 per month for his regular plan. How much in all will be Emmanuel’s charges for December?"""
    international_data_cost = 3.50
    days_in_december = 31
    regular_plan_cost = 175
    regular_plan_cost_per_day = regular_plan_cost / days_in_december
    international_data_cost_total = international_data_cost * 10
    total_cost = regular_plan_cost_per_day * 10 + international_data_cost_total
    result = total_cost
    return result

print(solution())