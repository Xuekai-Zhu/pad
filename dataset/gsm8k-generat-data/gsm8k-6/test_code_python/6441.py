def solution():
    # Calculate the total cost of buying presents for 8 friends
    friends_cost = 8 * 9

    # Calculate the remaining budget after buying presents for friends
    remaining_budget = 100 - friends_cost

    # Divide the remaining budget equally between Jaco's mother and father
    mother_father_budget = remaining_budget / 2

    result = mother_father_budget
    return result

print(solution())