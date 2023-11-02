def solution():
    # Calculate the total number of highlighters in Carrie's desk drawer
    yellow_highlighters = 7
    pink_highlighters = 7 + 7  # there are 7 more pink highlighters than yellow highlighters
    blue_highlighters = pink_highlighters + 5  # there are 5 more blue highlighters than pink highlighters
    total_highlighters = yellow_highlighters + pink_highlighters + blue_highlighters
    result = total_highlighters
    return result

print(solution())