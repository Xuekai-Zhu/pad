def solution():
    num_cheddar = 15
    num_mozzarella = 30
    num_pepperjack = 45
    total_sticks = num_cheddar + num_mozzarella + num_pepperjack

    # Calculate the percentage chance of picking a pepperjack stick
    percent_pepperjack = (num_pepperjack / total_sticks) * 100
    result = percent_pepperjack
    return result

print(solution())