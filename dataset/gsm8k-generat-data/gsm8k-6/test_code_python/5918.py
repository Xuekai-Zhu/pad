def solution():
    # Calculate the change in altitude during each stage of the balloon ride
    altitude_change_pulled = 50 * 15  # balloon rises at a rate of 50 feet per minute for 15 minutes
    altitude_change_released = -10 * 10  # balloon descends at a rate of 10 feet per minute for 10 minutes
    altitude_change_pulled_again = 50 * 15  # balloon rises at a rate of 50 feet per minute for another 15 minutes
    altitude_change_descend = -10 * 20  # balloon descends at a rate of 10 feet per minute for 20 minutes (after releasing chain)

    # Calculate the highest elevation reached by the balloon
    highest_elevation = altitude_change_pulled + altitude_change_released + altitude_change_pulled_again + altitude_change_descend
    result = highest_elevation
    return result

print(solution())