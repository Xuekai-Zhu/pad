def solution():
    # Define the original number of friends and cost per person
    original_friends = 10
    original_cost_per_person = x

    # Calculate the original total cost
    original_total_cost = original_friends * original_cost_per_person

    # Define the new number of friends and cost per person
    new_friends = original_friends - 4
    new_cost_per_person = original_cost_per_person + 8

    # Calculate the new total cost
    new_total_cost = new_friends * new_cost_per_person

    # The original and new total costs are the same, so we can equate them and solve for x
    original_total_cost = new_total_cost
    x = original_total_cost / original_friends

    # The gift cost is the original cost per person
    result = x
    return result

print(solution())