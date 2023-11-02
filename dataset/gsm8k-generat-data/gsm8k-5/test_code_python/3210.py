def solution():
    total_chargers = 24  # Anna has 24 chargers in total
    laptop_chargers = 5 * phone_chargers  # Anna has five times more laptop chargers than phone chargers

    # Solve for the number of phone chargers
    phone_chargers = (total_chargers - laptop_chargers) / 6
    result = phone_chargers
    return result

print(solution())