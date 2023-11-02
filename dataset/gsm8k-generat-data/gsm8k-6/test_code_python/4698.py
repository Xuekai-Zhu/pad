def solution():
    # Calculate the total number of masks used per day by Andrew's family
    masks_per_day = 5 * (100//20) / 4  # 100 masks divided among 5 family members, each using a mask every 4 days

    # Calculate the number of days it will take to finish the pack of masks
    days_to_finish = 100 / masks_per_day
    result = days_to_finish
    return result

print(solution())