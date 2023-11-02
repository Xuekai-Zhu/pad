def solution():
    """Kim's TV uses 125 watts of electricity per hour. She runs it for 4 hours a day. If electricity cost 14 cents per kw/h how many cents does her TV cost to run for a week?"""
    watts_per_hour = 125
    hours_per_day = 4
    days_per_week = 7

    # Calculate the total energy in kWh
    energy_in_kwh = watts_per_hour / 1000 * hours_per_day * days_per_week

    # Calculate the cost of electricity
    cost = energy_in_kwh * 14

    # Convert the cost from dollars to cents
    cost_in_cents = cost * 100

    result = cost_in_cents
    return result

print(solution())