def solution():
    # Define the facts about the Alamo and its location
    alamo_location = "San Antonio"
    alamo_battle_year = 1836
    # Check if there was a major battle in San Antonio in the 19th century
    if alamo_battle_year >= 1800 and alamo_battle_year <= 1899:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())