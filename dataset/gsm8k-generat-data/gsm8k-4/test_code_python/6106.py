def solution():
    """There are 8 men at a yoga studio with an average weight of 190 pounds and 6 women with an average weight of 120 pounds. What is the average weight of all 14 men and women?"""
    # Define the number of men and their average weight
    num_men = 8
    men_weight_avg = 190

    # Define the number of women and their average weight
    num_women = 6
    women_weight_avg = 120

    # Calculate the total weight of all men
    total_men_weight = num_men * men_weight_avg

    # Calculate the total weight of all women
    total_women_weight = num_women * women_weight_avg

    # Calculate the total weight of all men and women
    total_weight = total_men_weight + total_women_weight

    # Calculate the average weight of all men and women
    avg_weight = total_weight / (num_men + num_women)

    # return the result
    result = avg_weight
    return result

print(solution())