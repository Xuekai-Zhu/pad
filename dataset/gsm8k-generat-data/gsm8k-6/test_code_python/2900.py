def solution():
    # Solve for James' winnings
    remaining = 55  # James had $55 left over after donating and spending $2
    remaining += 2  # James spent $2 on a hot dog
    remaining *= 2  # James donated half of his winnings back to the charity
    winnings = remaining
    return winnings

print(solution())