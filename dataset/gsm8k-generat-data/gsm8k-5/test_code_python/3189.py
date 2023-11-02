def solution():
    # Calculate the total number of chickens after 2 years
    initial_chickens = 4  # Gary starts with 4 chickens
    final_chickens = 8 * initial_chickens  # After 2 years, he has 8 times as many chickens as he started with

    # Calculate the total number of eggs produced per day
    eggs_per_chicken = 6  # Each chicken lays 6 eggs per day
    total_eggs_per_day = final_chickens * eggs_per_chicken

    # Calculate the total number of eggs produced per week
    days_per_week = 7
    total_eggs_per_week = total_eggs_per_day * days_per_week
    result = total_eggs_per_week
    return result

print(solution())