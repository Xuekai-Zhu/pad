def solution():
    # Calculate the number of days the 2-liter bottle of soda will last
    soda_ml_per_day = 500  # ml of soda per day
    soda_ml_per_bottle = 2000  # ml in a 2-liter bottle
    days_lasts = soda_ml_per_bottle // soda_ml_per_day
    result = days_lasts
    return result

print(solution())