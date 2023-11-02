def solution():
    """There were 90 people at the summer picnic.  There were 50 soda cans, 50 plastic bottles of sparkling water, and 50 glass bottles of juice.  One-half of the guests drank soda, one-third of the guests drank sparkling water, and four-fifths of the juices were consumed.  How many recyclable cans and bottles were collected? """
    # Define the number of people at the picnic
    TOTAL_GUESTS = 90

    # Define the number of soda cans, plastic bottles of sparkling water, and glass bottles of juice
    SODA_CANS = 50
    SPARKLING_WATER_BOTTLES = 50
    JUICE_BOTTLES = 50

    # Calculate the number of guests that drank soda and the number of soda cans left over
    soda_drinkers = TOTAL_GUESTS // 2
    soda_cans_left = SODA_CANS - soda_drinkers

    # Calculate the number of guests that drank sparkling water and the number of plastic bottles left over
    sparkling_water_drinkers = TOTAL_GUESTS // 3
    sparkling_water_bottles_left = SPARKLING_WATER_BOTTLES - sparkling_water_drinkers

    # Calculate the number of juices consumed and the number of glass bottles left over
    juices_consumed = JUICE_BOTTLES * (4/5)
    juice_bottles_left = JUICE_BOTTLES - juices_consumed

    # Calculate the total number of recyclable cans and bottles collected
    total_recyclable = soda_cans_left + sparkling_water_bottles_left + juice_bottles_left

    # Display the total number of recyclable cans and bottles collected
    result = total_recyclable
    return result

print(solution())