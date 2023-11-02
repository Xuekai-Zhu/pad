def solution():
    adult_panda_daily_bamboo = 138  # an adult panda eats 138 pounds of bamboo each day
    baby_panda_daily_bamboo = 50  # a baby panda eats 50 pounds of bamboo a day
    days_per_week = 7  # there are 7 days in a week

    # Calculate the total bamboo eaten in a week by adults and babies
    total_bamboo = (adult_panda_daily_bamboo + baby_panda_daily_bamboo) * days_per_week

    result = total_bamboo
    return result

print(solution())