def solution():
    # Calculate the total mg of Tylenol James takes in a day
    mg_per_tablet = 375
    tablets_per_dose = 2
    doses_per_day = 24 // 6  # James takes the tablets every 6 hours, so he takes 4 doses in 24 hours
    total_mg_per_day = mg_per_tablet * tablets_per_dose * doses_per_day
    result = total_mg_per_day
    return result

print(solution())