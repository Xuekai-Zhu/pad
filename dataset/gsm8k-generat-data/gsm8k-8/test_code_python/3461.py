def solution():
    # Define the lion's and tiger's meat consumption per day
    lion_meat_per_day = 25
    tiger_meat_per_day = 20

    # Define the total amount of meat they have
    total_meat = 90

    # Calculate the total amount of meat they consume per day
    total_meat_per_day = lion_meat_per_day + tiger_meat_per_day

    # Calculate the number of days the meat will last
    days_lasts = total_meat / total_meat_per_day
    result = days_lasts
    return result

print(solution())