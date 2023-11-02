def solution():
    # Define the cost of one cup of coffee, one piece of cake, and one bowl of ice cream
    cost_coffee = 4
    cost_cake = 7
    cost_ice_cream = 3

    # Calculate the total cost for Mell's order
    mell_total_cost = 2 * cost_coffee + cost_cake

    # Calculate the total cost for each of Mell's friends
    friend_total_cost = mell_total_cost + 2 * cost_ice_cream

    # Calculate the total cost for Mell and her friends
    total_cost = mell_total_cost + friend_total_cost

    result = total_cost
    return result

print(solution())