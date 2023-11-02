def solution():
    # Calculate the total fuel needed for the empty plane
    empty_fuel = 20 * 400  # 20 gallons of fuel per mile, 400-mile trip

    # Calculate the additional fuel needed for passengers and crew
    passenger_fuel = (30 * 3 + 30 * 2 * 2) * 400  # 30 passengers, each with 2 bags, increasing fuel by 3 gallons per person and 2 gallons per bag
    crew_fuel = (5 * 3) * 400  # 5 flight crew, increasing fuel by 3 gallons per person

    # Calculate the total fuel needed for the trip
    total_fuel = empty_fuel + passenger_fuel + crew_fuel
    result = total_fuel
    return result

print(solution())