def solution():
    """A packet of candy sweets has 30 cherry-flavored sweets, 40 strawberry-flavored sweets, and 50 pineapple-flavored sweets. Aaron eats half of each of the flavored sweets and gives 5 cherry-flavored sweets to his friend. How many sweets are still in the packet of candy?"""
    # Define the initial number of each flavored sweet
    cherry_sweets = 30
    strawberry_sweets = 40
    pineapple_sweets = 50

    # Calculate the number of each sweet that Aaron eats
    cherry_eaten = cherry_sweets * 0.5
    strawberry_eaten = strawberry_sweets * 0.5
    pineapple_eaten = pineapple_sweets * 0.5

    # Subtract the eaten sweets and the sweets given to friend from the initial number of sweets
    cherry_sweets -= cherry_eaten + 5
    strawberry_sweets -= strawberry_eaten
    pineapple_sweets -= pineapple_eaten

    # Calculate the total number of sweets remaining in the packet
    total_sweets = cherry_sweets + strawberry_sweets + pineapple_sweets

    result = total_sweets
    return result

print(solution())