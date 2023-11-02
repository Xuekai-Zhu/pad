def solution():
    # Calculate the amount of milk pumped out of the storage tank
    pumped_out = 2,880 * 4

    # Calculate the amount of milk added to the storage tank
    added_in = 1,500 * 7

    # Calculate the total amount of milk that remained in the storage tank
    remaining = 30,000 - pumped_out + added_in

    result = remaining
    return result

print(solution())