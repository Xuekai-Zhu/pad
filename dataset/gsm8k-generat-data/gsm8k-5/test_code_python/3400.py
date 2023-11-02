def solution():
    combined_weight = 239  # Rodney, Roger and Ron can lift a combined weight of 239 pounds

    # Let Ron's lifting weight be "x"
    x = (combined_weight - 7) / (4 + 1 + 2)  # Roger can lift 7 pounds less than 4 times what Ron can lift
    # Rodney can lift twice as much as Roger, so his lifting weight is 2 * Roger's lifting weight
    rodney_weight = 2 * (4 * x - 7)

    result = rodney_weight
    return result

print(solution())