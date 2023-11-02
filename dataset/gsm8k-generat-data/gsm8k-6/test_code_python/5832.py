def solution():
    # Calculate the number of steaks sold by Harvey
    initial_steaks = 25  # initial number of steaks
    remaining_steaks = 12  # number of steaks left after selling some
    sold_steaks = initial_steaks - remaining_steaks  # number of steaks sold before selling 4 more
    sold_steaks += 4  # add the 4 more steaks sold
    result = sold_steaks
    return result

print(solution())