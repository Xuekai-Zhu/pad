def solution():
    total_bags = 3  # Jessica assumes it will take 3 bags of jelly beans to fill up the fishbowl
    red_in_bag = 24  # Jessica found 24 red jelly beans in her bag of jelly beans
    white_in_bag = 18  # Jessica found 18 white jelly beans in her bag of jelly beans

    # Calculate the percentage of red and white jelly beans in Jessica's bag
    total_in_bag = sum([red_in_bag, 13, 36, 28, 32, white_in_bag])
    percent_red_white = (red_in_bag + white_in_bag) / total_in_bag

    # Estimate the total number of red and white jelly beans in the fishbowl
    total_in_fishbowl = total_bags * total_in_bag
    estimate_red_white = percent_red_white * total_in_fishbowl
    result = estimate_red_white
    return result

print(solution())