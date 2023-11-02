def solution():
    """At the height of cranberry season, there are 60000 cranberries in a bog. 40% are harvested by humans and another 20000 are eaten by elk. How many cranberries are left?"""
    # Define the total number of cranberries in the bog
    total_cranberries = 60000

    # Calculate the number of cranberries harvested by humans
    human_harvest = total_cranberries * 0.4

    # Calculate the number of cranberries eaten by elk
    elk_eaten = 20000

    # Calculate the number of cranberries left
    cranberries_left = total_cranberries - human_harvest - elk_eaten

    # Return the result
    result = cranberries_left
    return result

print(solution())