def solution():
    # Calculate the total amount of garbage accumulated in two weeks
    accumulated_garbage = (3 * 200) * 2  # the garbage truck passes three times a week, collecting 200kg each time, for two weeks
    # Calculate the amount of garbage left around the dumpster after the first week
    accumulated_garbage -= (200 * 3)  
    # Calculate the amount of garbage produced during the second week (reduced by half)
    accumulated_garbage += ((200 * 3) / 2)

    result = accumulated_garbage
    return result

print(solution())