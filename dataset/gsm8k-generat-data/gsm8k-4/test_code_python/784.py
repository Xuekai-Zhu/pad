def solution():
    """The county fair was hosting a pumpkin contest to see who could grow the biggest pumpkin in pounds. Brad entered his pumpkin with a weight of 54 pounds. Jessica's was half the weight of Brad's. Betty's pumpkin weight 4 times the amount of Jessica's pumpkin. What is the difference between the heaviest and lightest pumpkin in pounds?"""
    # Define the weight of Brad's pumpkin
    brad_weight = 54

    # Calculate the weight of Jessica's pumpkin
    jessica_weight = brad_weight / 2

    # Calculate the weight of Betty's pumpkin
    betty_weight = jessica_weight * 4

    # Find the heaviest and lightest pumpkin weights
    heaviest_weight = max(brad_weight, jessica_weight, betty_weight)
    lightest_weight = min(brad_weight, jessica_weight, betty_weight)

    # Calculate the difference between the heaviest and lightest pumpkin weights
    difference = heaviest_weight - lightest_weight

    # return the result
    result = difference
    return result

print(solution())