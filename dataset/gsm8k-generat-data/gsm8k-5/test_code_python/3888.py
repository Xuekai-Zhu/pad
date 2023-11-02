def solution():
    april_cases = 20  # The store owner ordered 20 cases of soda in April
    may_cases = 30  # The store owner ordered 30 cases of soda in May
    bottles_per_case = 20  # Each case contains 20 bottles of soda

    # Calculate the total number of bottles of soda ordered in April and May
    total_bottles = (april_cases + may_cases) * bottles_per_case
    result = total_bottles
    return result

print(solution())