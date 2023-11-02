def solution():
    """In Carrie's desk drawer there are 7 yellow highlighters. There are 7 more pink highlighters than yellow highlighters, and there are 5 more blue highlighters than pink highlighters. How many highlighters are in Carrie's desk drawer in all?"""
    # Define the number of yellow highlighters
    yellow_highlighters = 7

    # Calculate the number of pink highlighters
    pink_highlighters = yellow_highlighters + 7

    # Calculate the number of blue highlighters
    blue_highlighters = pink_highlighters + 5

    # Calculate the total number of highlighters
    total_highlighters = yellow_highlighters + pink_highlighters + blue_highlighters

    # Return the result
    result = total_highlighters
    return result

print(solution())