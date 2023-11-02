def solution():
    total_money = 90  # Kiki currently has $90
    scarf_price = 2  # Each scarf costs $2
    hats_to_scarfs_ratio = 2  # Kiki buys twice as many hats as scarves

    # Determine how much Kiki spends on hats and how much she spends on scarves
    hat_spending_percentage = 60  # Kiki spends 60% of her money on hats
    hat_spending = total_money * (hat_spending_percentage / 100)
    scarf_spending = total_money - hat_spending

    # Calculate how many scarves Kiki can buy with the money she spent on them
    scarf_count = scarf_spending / scarf_price

    # Calculate how many hats Kiki bought
    hat_count = scarf_count * hats_to_scarfs_ratio

    result = scarf_count
    return result

print(solution())