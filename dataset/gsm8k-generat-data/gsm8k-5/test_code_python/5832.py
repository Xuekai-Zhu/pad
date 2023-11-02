def solution():
    initial_steaks = 25  # Harvey started with 25 steaks
    remaining_steaks = 12  # Harvey had 12 steaks left after selling some

    # Calculate the number of steaks sold
    sold_steaks = initial_steaks - remaining_steaks

    # Harvey sold 4 more steaks after having 12 left
    sold_steaks += 4

    result = sold_steaks
    return result

print(solution())