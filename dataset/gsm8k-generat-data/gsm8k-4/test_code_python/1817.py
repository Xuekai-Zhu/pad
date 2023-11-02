def solution():
    """Carson is refilling his tires. Each tire can hold 500 cubic inches of air. Two of the tires are completely flat and empty. One tire is 40% full and the last tire is 70% full. If Carson injects 50 cubic inches of air with each pump, how many pumps will it take him to fill all the tires?"""
    # Define the capacity of each tire, in cubic inches
    TIRE_CAPACITY = 500

    # Define the initial volume of air in each tire, in cubic inches
    tire1_vol = 0
    tire2_vol = 0
    tire3_vol = TIRE_CAPACITY * 0.4
    tire4_vol = TIRE_CAPACITY * 0.7

    # Calculate the total volume of air needed to fill all the tires
    total_vol = (4 * TIRE_CAPACITY) - (tire3_vol + tire4_vol)

    # Calculate the number of pumps needed to fill all the tires
    num_pumps = total_vol / 50

    # Round up to the nearest integer
    num_pumps = math.ceil(num_pumps)

    result = num_pumps
    return result

print(solution())