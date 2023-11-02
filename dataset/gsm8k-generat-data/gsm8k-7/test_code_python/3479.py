def solution():
    photo_earnings = 15
    shark_frequency = 1/10    # sharks seen per minute
    fuel_cost_per_hour = 50
    shark_hunting_hours = 5

    # Calculate the total number of sharks seen in 5 hours
    total_sharks_seen = (shark_frequency * 60) * shark_hunting_hours

    # Calculate the total earnings from taking photos of sharks
    total_earnings = total_sharks_seen * photo_earnings

    # Calculate the total fuel cost
    total_fuel_cost = fuel_cost_per_hour * shark_hunting_hours

    # Calculate the total profit
    total_profit = total_earnings - total_fuel_cost
    result = total_profit
    return result

print(solution())