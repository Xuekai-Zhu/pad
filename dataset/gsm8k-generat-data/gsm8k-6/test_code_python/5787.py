def solution():
    original_price = 1.6  # price per pound of apples before the increase
    increase_percentage = 25  # the price got raised by 25%
    new_price = original_price + (original_price * (increase_percentage / 100))  # calculate the new price
    cost_per_person = 2 * new_price  # cost of 2 pounds of apples for each person
    total_cost = cost_per_person * 4  # total cost for a 4 member family
    result = total_cost
    return result

print(solution())