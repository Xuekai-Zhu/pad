def solution():
    num_quarters = 35  # Nick has 35 quarters
    state_quarters = int(num_quarters * (2/5))  # 2/5 of the quarters are state quarters
    penn_quarters = int(state_quarters * (1/2))  # 50 percent of the state quarters are Pennsylvania quarters
    result = penn_quarters
    return result

print(solution())