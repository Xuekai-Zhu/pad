def solution():
    # Calculate the cost per shirt for Jessica
    cost_per_shirt_jessica = 20/2

    # Calculate the total cost of shirts and pants for Peter
    total_cost_peter = 62 - 5 * cost_per_shirt_jessica

    # Calculate the cost per pair of pants for Peter
    cost_per_pants_peter = total_cost_peter / 2
    result = cost_per_pants_peter
    return result

print(solution())