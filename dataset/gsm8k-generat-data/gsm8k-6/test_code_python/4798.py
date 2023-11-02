def solution():
    # Calculate how much milk was pumped out of the tank
    milk_pumped = 2880 * 4

    # Calculate how much milk was added to the tank
    milk_added = 1500 * 7

    # Calculate how much milk is left in the storage tank
    milk_left = 30000 - milk_pumped + milk_added
    result = milk_left
    return result

print(solution())