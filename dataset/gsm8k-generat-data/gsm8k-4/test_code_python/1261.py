def solution():
    """Chastity made 12 angel food cakes to give to friends.  She placed the cakes in boxes, and then walked them out to her car.  But she had forgotten her keys.  So, she placed the boxes of cakes in one stack on the hood of her car, and then she ran back into the house to get her keys.  But before she returned, a black crow came, landed on the stack of cakes, and knocked over half of the stack.  When Chastity returned, she picked up half of the fallen cakes, which were not damaged, but the rest of the cakes were destroyed.  How many cakes were destroyed?"""
    # Define the initial number of cakes
    initial_cakes = 12

    # Calculate the number of cakes knocked over by the crow
    knocked_cakes = initial_cakes // 2

    # Calculate the number of cakes picked up by Chastity
    picked_up_cakes = knocked_cakes // 2

    # Calculate the number of cakes destroyed
    destroyed_cakes = initial_cakes - picked_up_cakes - knocked_cakes

    result = destroyed_cakes
    return result

print(solution())