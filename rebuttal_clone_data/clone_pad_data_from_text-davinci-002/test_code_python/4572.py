def solution():
     ounces_per_bottle = 16
     hours_awake = 16
     bottles_per_day = hours_awake / 4
     twice_daily_bottle = (ounces_per_bottle * 1.25)
     total_daily_fluid = (bottles_per_day * ounces_per_bottle) + twice_daily_bottle
     fluid_per_week = total_daily_fluid * 7
 
     return fluid_per_week

print(solution())