def solution():
    # Define the amount of milk each cow produces per day
    bess_daily_milk = 2
    brownie_daily_milk = 3 * bess_daily_milk
    daisy_daily_milk = bess_daily_milk + 1

    # Calculate the total amount of milk per week for each cow
    bess_weekly_milk = bess_daily_milk * 7
    brownie_weekly_milk = brownie_daily_milk * 7
    daisy_weekly_milk = daisy_daily_milk * 7

    # Calculate the total amount of milk per week from all the cows
    total_weekly_milk = bess_weekly_milk + brownie_weekly_milk + daisy_weekly_milk
    result = total_weekly_milk
    return result

print(solution())