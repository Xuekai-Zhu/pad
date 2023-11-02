def solution():
    # Calculate the total cost of the shorts and shoes
    shorts_cost = 5 * 7
    shoes_cost = 2 * 10
    total_cost = shorts_cost + shoes_cost + 75

    # Calculate the total cost of the tops
    top_cost = (total_cost - shorts_cost - shoes_cost) / 4
    result = top_cost
    return result

print(solution())