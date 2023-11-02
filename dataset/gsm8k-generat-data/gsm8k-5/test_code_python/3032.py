def solution():
    # Harvest on Wednesday
    harvest_wed = 400

    # Harvest on Thursday
    harvest_thu = harvest_wed / 2

    # Total harvest
    total_harvest = 2000

    # Harvest on Friday
    harvest_fri = total_harvest - harvest_wed - harvest_thu

    # Tomatoes remaining after giving away to friends
    remaining_tomatoes = harvest_fri - 700
    result = remaining_tomatoes
    return result

print(solution())