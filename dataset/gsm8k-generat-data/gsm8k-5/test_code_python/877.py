def solution():
    brother_picked = 3 * 15  # Kimberly's brother picked 3 baskets, each containing 15 strawberries
    kimberly_picked = 8 * brother_picked  # Kimberly picked 8 times the amount her brother picked
    parents_picked = kimberly_picked - 93  # Kimberly's parents picked 93 less than Kimberly

    total_picked = brother_picked + kimberly_picked + parents_picked  # Calculate the total number of strawberries picked
    strawberries_each = total_picked / 4  # Divide the total number of strawberries equally among 4 people
    result = int(strawberries_each)
    return result

print(solution())