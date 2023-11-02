def solution():
    total_cost = 500  # Cost of the new PlayStation is $500
    total_savings = 200 + 150  # Percy has already saved $200 on his birthday and $150 at Christmas
    remaining_cost = total_cost - total_savings  # Percy needs to save the remaining cost

    # Calculate the number of games Percy needs to sell to reach his goal
    games_needed = remaining_cost / 7.5
    result = games_needed
    return result

print(solution())