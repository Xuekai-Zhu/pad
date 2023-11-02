def solution():
    total_cranberries = 60000
    human_harvest = 0.4 * total_cranberries
    elk_eaten = 20000

    # Calculate the number of cranberries left
    cranberries_left = total_cranberries - human_harvest - elk_eaten
    result = cranberries_left
    return result

print(solution())