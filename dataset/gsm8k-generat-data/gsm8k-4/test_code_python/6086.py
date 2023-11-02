def solution():
    """John buys 20 candy bars. His brother Dave pays for 6 of them. If each candy bar costs $1.50, how much did John pay?"""
    # Define the total number of candy bars
    total_candy_bars = 20

    # Define the number of candy bars paid for by Dave
    daves_candy_bars = 6

    # Calculate the number of candy bars paid for by John
    johns_candy_bars = total_candy_bars - daves_candy_bars

    # Calculate the total cost of candy bars paid for by John
    johns_cost = johns_candy_bars * 1.5

    # return the result
    result = johns_cost
    return result

print(solution())