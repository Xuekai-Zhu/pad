def solution():
    eggs_per_day_1 = 3  # Chester eats 3 eggs per day for 30 days
    eggs_per_day_2 = 5  # Chester increases the eggs to 5 eggs per day for 30 days
    days_1 = 30  # Chester wants to know how many dozens of eggs Chester will need for 60 days

    # Calculate the total number of eggs Chester will eat in 60 days
    total_eggs_1 = eggs_per_day_1 * days_1

    # Calculate the total number of eggs Chester will eat in 60 days
    total_eggs_2 = eggs_per_day_2 * days_2

    # Calculate the total number of dozens of eggs Chester will need for 60 days
    total_dozens = total_eggs_1 + total_eggs_2
    result = total_dozens
    return result

print(solution())