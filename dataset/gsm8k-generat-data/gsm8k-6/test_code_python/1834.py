def solution():
    # Calculate the total cost of lodging for Jimmy
    hostel_cost = 15 * 3  # Jimmy stays in the hostel for the first 3 days at $15 per night
    cabin_cost_per_person = 45 / 3  # Jimmy and his two friends share the cost of the cabin at $45 total per night
    cabin_cost = cabin_cost_per_person * 2  # Jimmy pays for himself and one of his friends
    total_cost = hostel_cost + cabin_cost  # calculate the total cost of lodging

    result = total_cost
    return result

print(solution())