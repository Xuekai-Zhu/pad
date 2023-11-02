def solution():
    # Calculate the total amount of kibble Luna ate in one day
    total_kibble = 1 + 1 + 1 + 2  # Mary gave 1 cup in the morning and 1 cup in the evening; Frank gave 1 cup in the afternoon and 2 cups in the late evening
    # Calculate the amount of kibble left in the bag
    remaining_kibble = 12 - total_kibble  # start with a 12-cup bag and subtract the total kibble Luna ate
    result = remaining_kibble
    return result

print(solution())