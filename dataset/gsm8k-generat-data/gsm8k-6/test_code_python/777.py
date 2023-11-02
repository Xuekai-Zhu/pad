def solution():
    # Calculate the total cost of tickets for the carnival rides
    cost_Mara_bumper = 2 * 2  # Mara rode the bumper car two times, each ticket costs $2
    cost_Riley_shuttle = 4 * 4  # Riley rode the space shuttle four times, each ticket costs $4
    cost_Ferris_wheel = 3 * (5 + 5)  # Mara and Riley rode the Ferris wheel three times each, each ride costs $5
    total_cost = cost_Mara_bumper + cost_Riley_shuttle + cost_Ferris_wheel
    result = total_cost
    return result

print(solution())