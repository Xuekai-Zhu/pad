def solution():
    current_collection = 40
    desired_percent_increase = 20
    desired_amount = current_collection + (current_collection * (desired_percent_increase / 100))
    result = desired_amount
    return result

print(solution())