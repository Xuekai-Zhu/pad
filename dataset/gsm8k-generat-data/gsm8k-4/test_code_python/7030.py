def solution():
    """Sally was at a self-serve candy shop where you scoop candy from the bins and pay based on the weight. She scoops 32 cherry sours into a bag. Then she gets a scoop of lemon sours, and the ratio of cherry sours to lemon sours is 4:5. Then she gets a scoop of orange sours, and they make up 25% of the sours in the bag. How many sours does she have in total?"""
    # Define the initial number of cherry sours
    cherry_sours = 32
    total_sours = None

    # Calculate the number of lemon sours
    lemon_sours = cherry_sours * (5/4) - cherry_sours
    
    # Calculate the total number of sours
    total_sours = cherry_sours + lemon_sours

    # Calculate the number of orange sours
    orange_sours = total_sours * 0.25

    # Calculate the total number of sours
    total_sours += orange_sours

    result = round(total_sours)
    return result

print(solution())