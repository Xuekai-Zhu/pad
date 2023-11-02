def solution():
    # Calculate how many cakes Louise has already produced
    cakes_produced = 60/2  

    # Calculate how many cakes she has left to make after baking half the remaining amount
    cakes_left = (60 - cakes_produced)/2  

    # Calculate how many cakes she has left to make after baking a third of the remaining amount
    cakes_left = cakes_left - cakes_left/3  

    result = cakes_left
    return result

print(solution())