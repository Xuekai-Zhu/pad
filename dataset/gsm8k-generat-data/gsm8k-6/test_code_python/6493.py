def solution():
    # Calculate the amount of flour Michael doesn't need
    excess_flour = 8 - 6  # Michael has an 8 cup bag of flour and needs 6 cups of flour

    # Calculate the number of 1/4 cup scoops Michael needs to remove
    scoops_to_remove = excess_flour / (1/4)  # Each scoop is 1/4 cup

    result = scoops_to_remove
    return result

print(solution())