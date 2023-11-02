def solution():
    # Calculate the number of trout Henry caught
    trout = 3 * 16

    # Calculate the number of fish Henry returns
    returned = 0.5 * trout

    # Calculate the total number of fish they have now
    total_fish = 16 + 10 + trout - returned
    result = total_fish
    return result

print(solution())