def solution():
    # Calculate the total contribution for Harry's party
    total_contribution = 3 * (30 + (3/4 * 7 * 3))  # Harry's birthday was three weeks after the closing of the school, which is 3/4 of a month. Each of Harry's friends contributed the same amount
    contribution_per_friend = total_contribution / 3
    result = contribution_per_friend
    return result

print(solution())