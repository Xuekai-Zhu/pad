def solution():
    flowers_per_day = 60  # Miriam can take care of 60 flowers in one day
    hours_per_day = 5  # Miriam works 5 hours a day
    days_of_work = 6  # Miriam will work for 6 days

    # Calculate the total number of flowers Miriam can take care of in 6 days of work
    total_flowers = flowers_per_day * hours_per_day * days_of_work
    result = total_flowers
    return result

print(solution())