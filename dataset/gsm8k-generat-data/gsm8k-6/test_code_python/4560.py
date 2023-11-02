def solution():
    # Calculate the total number of days in 4 years with no leap year
    total_days = 4 * 365  # 4 years with no leap year

    # Calculate the number of comics James writes every other day
    comics_per_day = 1/2
    total_comics = comics_per_day * total_days  # number of comics written in 4 years

    result = total_comics
    return result

print(solution())