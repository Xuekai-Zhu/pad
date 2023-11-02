def solution():
    """Jonathan ran 7.5 kilometers. Mercedes ran twice that distance and Davonte ran 2 kilometers farther than Mercedes. How many kilometers did Mercedes and Davonte run in total?"""
    # Define the distance Jonathan ran
    jonathan_distance = 7.5

    # Define the distance Mercedes ran, which is twice the distance Jonathan ran
    mercedes_distance = jonathan_distance * 2

    # Define the distance Davonte ran, which is 2 kilometers more than the distance Mercedes ran
    davonte_distance = mercedes_distance + 2

    # Calculate the total distance that Mercedes and Davonte ran
    total_distance = mercedes_distance + davonte_distance

    # return the result
    result = total_distance
    return result

print(solution())