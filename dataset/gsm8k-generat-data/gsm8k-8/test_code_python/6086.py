def solution():
    # Define the number of candy bars John bought and the number his brother paid for
    john_candy_bars = 20
    dave_candy_bars = 6

    # Calculate the total cost of John's candy bars
    john_cost = (john_candy_bars - dave_candy_bars) * 1.5

    result = john_cost
    return result

print(solution())