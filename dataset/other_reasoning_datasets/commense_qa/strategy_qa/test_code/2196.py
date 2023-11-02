def solution():
    # Define the cost per visit and the number of visits
    visit_cost = 17
    num_visits = 20
    # Define the maximum amount Bernie Sanders can pay for 20 visits
    max_cost = 200
    # Check if the total cost is less than the maximum amount
    if visit_cost * num_visits < max_cost:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())