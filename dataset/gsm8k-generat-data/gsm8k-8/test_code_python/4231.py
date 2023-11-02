def solution():
    # Define the number of men and Olaf's daily water needs
    num_men = 25
    water_per_man_per_day = 0.5

    # Calculate the total water needed for the entire journey
    total_water_needed = num_men * water_per_man_per_day * 4000

    # Calculate the number of days the journey will take
    num_days = 4000 / 200

    # Calculate the total water needed per day
    water_per_day = total_water_needed / num_days

    result = water_per_day
    return result

print(solution())