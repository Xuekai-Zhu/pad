def solution():
    """Three builders build a single floor of a house in 30 days. If each builder is paid $100 for a single day’s work, how much would it cost to hire 6 builders to build 5 houses with 6 floors each?"""
    # Define the number of builders and days to build a single floor
    NUM_BUILDERS = 3
    DAYS_PER_FLOOR = 30

    # Define the number of houses and floors to be built
    NUM_HOUSES = 5
    NUM_FLOORS_PER_HOUSE = 6

    # Define the cost per builder per day
    COST_PER_DAY = 100

    # Calculate the number of floors to be built
    total_floors = NUM_HOUSES * NUM_FLOORS_PER_HOUSE

    # Calculate the number of days it would take 6 builders to build a single floor
    days_per_floor_6_builders = (NUM_BUILDERS / 6) * DAYS_PER_FLOOR

    # Calculate the total cost to hire 6 builders to build all the floors
    total_cost = total_floors * 6 * days_per_floor_6_builders * COST_PER_DAY

    # Display the total cost
    result = total_cost
    return result

print(solution())