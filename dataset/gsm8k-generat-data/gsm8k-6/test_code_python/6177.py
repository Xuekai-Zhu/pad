def solution():
    # Calculate the number of brownies left after the children ate 25% of them
    brownies = 16
    brownies_after_children = (3/4) * brownies  

    # Calculate the number of brownies left after the family ate 50% of them
    brownies_after_family = (1/2) * brownies_after_children  

    # Calculate the total number of brownies left after Lorraine ate 1 more
    total_brownies_left = brownies_after_family - 1  
    result = total_brownies_left
    return result

print(solution())