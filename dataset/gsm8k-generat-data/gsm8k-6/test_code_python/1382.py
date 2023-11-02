def solution():
    # Calculate the total cost after the first year, split evenly between two people
    total_cost = 14 * 12  # $14 a month for 12 months
    cost_per_person = total_cost / 2  # evenly splitting the cost with one friend
    result = cost_per_person
    return result

print(solution())