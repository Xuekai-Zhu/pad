def solution():
    good_week_sale = 800 * 2  # Haji's mother sells goods worth $800, which is half the amount she sells on a good week
    tough_week_sale = 800  # Haji's mother sells goods worth $800 on a tough week
    num_good_weeks = 5  # Haji's mother has 5 good weeks
    num_tough_weeks = 3  # Haji's mother has 3 tough weeks

    # Calculate the total sale during good weeks and tough weeks
    total_sale_good_weeks = good_week_sale * num_good_weeks
    total_sale_tough_weeks = tough_week_sale * num_tough_weeks

    # Calculate the total amount of money Haji's mother makes
    total_sale = total_sale_good_weeks + total_sale_tough_weeks
    result = total_sale
    return result

print(solution())