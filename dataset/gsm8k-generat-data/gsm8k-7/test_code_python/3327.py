def solution():
    spent_amount = 250
    gems_per_dollar = 100
    bonus_percentage = 20

    # Calculate the total number of gems Tom bought
    total_gems = spent_amount * gems_per_dollar

    # Calculate the bonus amount of gems Tom received
    bonus_gems = total_gems * (bonus_percentage / 100)

    # Add the bonus gems to the total gems bought
    total_gems += bonus_gems
    result = total_gems
    return result

print(solution())