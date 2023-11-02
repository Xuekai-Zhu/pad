def solution():
    """At the height of cranberry season, there are 60000 cranberries in a bog. 40% are harvested by humans and another 20000 are eaten by elk. How many cranberries are left?"""
    # Define the total number of cranberries in the bog
    total_cranberries = 60000

    # Calculate the number of cranberries harvested by humans
    harvested_cranberries = int(total_cranberries * 0.4)

    # Calculate the number of cranberries eaten by elk
    eaten_cranberries = 20000

    # Calculate the number of cranberries left in the bog
    remaining_cranberries = total_cranberries - harvested_cranberries - eaten_cranberries

    # Display the number of cranberries left
    result = remaining_cranberries
    return result

print(solution())