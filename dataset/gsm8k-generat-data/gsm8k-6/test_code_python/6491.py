def solution():
    # Calculate the total cost of the cable program
    cost_first_100 = 100  # cost of first 100 channels
    cost_next_100 = 100/2  # cost of next 100 channels
    total_cost = cost_first_100 + cost_next_100  # total cost of cable program
    per_person_cost = total_cost / 2  # cost split evenly between James and roommate
    result = per_person_cost
    return result

print(solution())