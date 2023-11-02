def solution():
    # Find Wanda's current weight
    wanda_weight = 220  # given in the problem
    # Find Yola's current weight by subtracting 30 from Wanda's weight
    yola_weight = wanda_weight - 30
    # Find Yola's weight 2 years ago by subtracting 80 from Wanda's weight 2 years ago
    yola_weight_2_years_ago = wanda_weight - 80
    result = yola_weight_2_years_ago
    return result

print(solution())