def solution():
    """When Doctor Lindsay works in her office, she usually sees 4 adult patients and 3 child patients every hour. If the cost for an adult's office visit is $50, and the cost for a child's office visit is $25, how much money, in dollars, does Doctor Lyndsay receive in a typical 8-hour day for seeing all her patients?"""
    adults_per_hour = 4
    children_per_hour = 3
    adult_cost = 50
    child_cost = 25
    total_hours = 8
    total_adults = adults_per_hour * total_hours
    total_children = children_per_hour * total_hours
    total_money = (total_adults * adult_cost) + (total_children * child_cost)
    result = total_money
    return result

print(solution())