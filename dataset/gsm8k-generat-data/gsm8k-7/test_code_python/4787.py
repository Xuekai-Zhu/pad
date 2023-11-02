def solution():
    lizard_value = 8
    water_value = 5/3 # 3 lizards = 5 gallons
    horse_value = 80 # 1 horse = 80 gallons

    bottlecap_income_per_day = 20
    bottlecap_expense_per_night = 4

    # Calculate the number of bottlecaps Marla earns each day (income minus expenses)
    net_bottlecap_income_per_day = bottlecap_income_per_day - bottlecap_expense_per_night

    # Calculate the number of bottlecaps she needs to buy a horse
    bottlecaps_needed_for_horse = horse_value / water_value * lizard_value

    # Calculate the number of days needed to collect enough bottlecaps
    days_needed = bottlecaps_needed_for_horse / net_bottlecap_income_per_day
    result = days_needed
    return result

print(solution())