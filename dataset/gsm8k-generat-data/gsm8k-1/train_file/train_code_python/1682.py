def solution():
    """In Carrie's desk drawer there are 7 yellow highlighters. There are 7 more pink highlighters than yellow highlighters, and there are 5 more blue highlighters than pink highlighters. How many highlighters are in Carrie's desk drawer in all?"""
    yellow_highlighters = 7
    pink_highlighters = yellow_highlighters + 7
    blue_highlighters = pink_highlighters + 5
    total_highlighters = yellow_highlighters + pink_highlighters + blue_highlighters
    result = total_highlighters
    return result

print(solution())