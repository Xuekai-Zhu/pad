def solution():
    total_bottles = 550  # Don is capable of buying only 550 bottles
    bottles_A = 150  # Shop A normally sells 150 bottles to Don
    bottles_B = 180  # Shop B sells 180 bottles to Don
    # Calculate the number of bottles Don buys from Shop C
    bottles_C = total_bottles - bottles_A - bottles_B
    result = bottles_C
    return result

print(solution())