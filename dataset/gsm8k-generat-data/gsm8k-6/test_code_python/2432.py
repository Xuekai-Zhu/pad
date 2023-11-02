def solution():
    # Calculate the number of brownies Annie had left after giving some away
    half_brownies = 20 * 0.5  # half of the 20 brownies
    remaining_brownies = 20 - half_brownies  # remaining brownies
    friend_brownies = remaining_brownies * 0.5  # brownies given to Carl
    remaining_brownies -= (friend_brownies + 2)  # brownies given to Simon and his friend
    result = remaining_brownies
    return result

print(solution())