def solution():
    """Sally was at a self-serve candy shop where you scoop candy from the bins and pay based on the weight. She scoops 32 cherry sours into a bag. Then she gets a scoop of lemon sours, and the ratio of cherry sours to lemon sours is 4:5. Then she gets a scoop of orange sours, and they make up 25% of the sours in the bag. How many sours does she have in total?"""
    # Define the ratio of cherry sours to lemon sours
    cherry_to_lemon = 4/5

    # Calculate the number of lemon sours
    lemon_sours = round(32 * cherry_to_lemon)

    # Calculate the total number of sours in the bag (excluding orange sours)
    total_sours = 32 + lemon_sours

    # Calculate the number of orange sours
    orange_sours = round(total_sours * 0.25)

    # Calculate the total number of sours
    all_sours = total_sours + orange_sours

    # Display the total number of sours
    result = all_sours
    return result

print(solution())