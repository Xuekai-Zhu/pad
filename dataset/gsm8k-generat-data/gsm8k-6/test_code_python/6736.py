def solution():
    # Calculate the total cost of carnations bought by Georgia
    cost_one = 0.50  # cost of one carnation
    cost_dozen = 4.00  # cost of one dozen carnations
    dozens_for_teachers = 5  # dozens of carnations for 5 teachers
    carnations_for_friends = 14  # carnations for 14 friends

    total_carnations = dozens_for_teachers * 12 + carnations_for_friends  # total number of carnations bought
    # Calculate the total cost of carnations bought
    total_cost = (dozens_for_teachers * cost_dozen) + (carnations_for_friends * cost_one)
    result = total_cost
    return result

print(solution())