def solution():
    """At the height of cranberry season, there are 60000 cranberries in a bog. 40% are harvested by humans and 
    another 20000 are eaten by elk. How many cranberries are left?"""
    total_cranberries = 60000
    harvested_cranberries = 0.4 * total_cranberries
    elk_eaten_cranberries = 20000
    remaining_cranberries = total_cranberries - harvested_cranberries - elk_eaten_cranberries
    result = remaining_cranberries
    return result

print(solution())