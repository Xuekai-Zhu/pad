def solution():
    # Calculate the total cost of the gifts before rebate
    total_cost = (3 * 26) + (2 * 83) + 90

    # Subtract the rebate from the total cost to get the final cost
    final_cost = total_cost - 12

    result = final_cost
    return result

print(solution())