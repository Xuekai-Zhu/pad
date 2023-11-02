def solution():
    # Calculate the total cost of the meal
    total_cost = (5 * 3) + (4 * 1.2) + (5 * 0.5) + 2.7  # 5 pieces of hamburger at $3 each, 4 sets of French fries at $1.2 each, 5 cups of soda at $0.5 each, 1 platter of spaghetti at $2.7
    num_friends = 5  # 5 friends split the bill equally
    cost_per_friend = total_cost / num_friends
    result = cost_per_friend
    return result

print(solution())