def solution():
    """If a solver flips a coin 211 times and gets a head on 65 of the flips, how many more tails than heads did he get?"""
    # Define the number of coin flips and heads
    total_flips = 211
    heads = 65

    # Calculate the number of tails
    tails = total_flips - heads

    # Calculate the difference between tails and heads
    difference = tails - heads

    result = abs(difference)
    return result

print(solution())