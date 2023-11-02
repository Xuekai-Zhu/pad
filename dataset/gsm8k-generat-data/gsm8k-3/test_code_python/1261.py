def solution():
    """Chastity made 12 angel food cakes to give to friends.  She placed the cakes in boxes, and then walked them out to her car.  But she had forgotten her keys.  So, she placed the boxes of cakes in one stack on the hood of her car, and then she ran back into the house to get her keys.  But before she returned, a black crow came, landed on the stack of cakes, and knocked over half of the stack.  When Chastity returned, she picked up half of the fallen cakes, which were not damaged, but the rest of the cakes were destroyed.  How many cakes were destroyed?"""
    # Define the number of cakes Chastity made
    total_cakes = 12

    # Calculate the number of cakes in the half of the stack that was knocked over
    knocked_over_cakes = total_cakes // 2

    # Calculate the number of undamaged cakes that Chastity picked up
    undamaged_cakes = knocked_over_cakes // 2

    # Calculate the number of destroyed cakes
    destroyed_cakes = total_cakes - undamaged_cakes - knocked_over_cakes

    # Display the number of destroyed cakes
    result = destroyed_cakes
    return result

print(solution())