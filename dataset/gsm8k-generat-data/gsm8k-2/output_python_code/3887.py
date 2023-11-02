def solution():
    """A store owner ordered 20 cases of bottles of soda in April and 30 cases in May. There are 20 bottles per case. How many bottles of soda did the store owner order in April and May?"""
    bottles_per_case = 20
    april_cases = 20
    may_cases = 30
    total_bottles = (april_cases + may_cases) * bottles_per_case
    result = total_bottles
    return result

print(solution())