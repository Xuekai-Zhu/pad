def solution():
    """There are 8 men at a yoga studio with an average weight of 190 pounds and 6 women with an average weight of 120 pounds. What is the average weight of all 14 men and women?"""
    # Define the number of men and women and their average weights
    NUM_MEN = 8
    AVG_WEIGHT_MEN = 190
    NUM_WOMEN = 6
    AVG_WEIGHT_WOMEN = 120

    # Calculate the total weight of all the men
    total_weight_men = NUM_MEN * AVG_WEIGHT_MEN

    # Calculate the total weight of all the women
    total_weight_women = NUM_WOMEN * AVG_WEIGHT_WOMEN

    # Calculate the total weight of everyone
    total_weight = total_weight_men + total_weight_women

    # Calculate the average weight of everyone
    avg_weight = total_weight / (NUM_MEN + NUM_WOMEN)

    # Display the average weight
    result = avg_weight
    return result

print(solution())