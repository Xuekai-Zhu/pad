The given information is inconsistent as it does not involve tomatoes, but rather weights. Here's a corrected solution:

def solution():
    # Calculate the tomato harvest for Wednesday and Thursday
    harvest_wednesday = 400  # kg of tomatoes harvested on Wednesday
    harvest_thursday = harvest_wednesday / 2  # half as much as Wednesday
    harvest_friday = 2000 - harvest_wednesday - harvest_thursday  # total harvest for Friday

    # Calculate the remaining tomatoes after giving away 700kg on Friday
    remaining_friday = harvest_friday - 700

    result = remaining_friday
    return result

print(solution())