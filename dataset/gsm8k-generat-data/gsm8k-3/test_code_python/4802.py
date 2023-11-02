def solution():
    """The battery charge in Mary’s cordless vacuum cleaner lasts ten minutes. It takes her four minutes to vacuum each room in her house. Mary has three bedrooms, a kitchen, and a living room. How many times does Mary need to charge her vacuum cleaner to vacuum her whole house?"""
    # Define the battery charge and vacuuming time per room
    BATTERY_CHARGE = 10
    VACUUM_TIME = 4

    # Define the number of rooms in Mary's house
    NUM_ROOMS = 5

    # Calculate the total vacuuming time needed for the house
    total_vacuum_time = VACUUM_TIME * NUM_ROOMS

    # Calculate the number of times Mary needs to charge her vacuum cleaner
    num_charges = total_vacuum_time / BATTERY_CHARGE

    # Round up to the nearest whole number
    num_charges = math.ceil(num_charges)

    # Display the number of times Mary needs to charge her vacuum cleaner
    result = num_charges
    return result

print(solution())