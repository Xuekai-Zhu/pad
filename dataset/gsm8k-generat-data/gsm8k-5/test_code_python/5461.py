def solution():
    total_clovers = 200  # June picks 200 clovers in total
    three_petals = 0.75 * total_clovers  # 75% of cloves have 3 petals
    two_petals = 0.24 * total_clovers  # 24% of cloves have 2 petals
    four_petals = 0.01 * total_clovers  # 1% of cloves have 4 petals

    # Calculate the total number of cents June earns
    total_cents = three_petals + two_petals + four_petals
    result = total_cents
    return result

print(solution())