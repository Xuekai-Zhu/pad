def solution():
    # Calculate the number of swordfish caught by Shelly each time
    shelly_catch = 5 * 5 - 2

    # Calculate the number of swordfish caught by Sam each time
    sam_catch = shelly_catch - 1

    # Calculate the total number of swordfish caught by both together
    total_catch = (shelly_catch + sam_catch) * 5

    result = total_catch
    return result

print(solution())