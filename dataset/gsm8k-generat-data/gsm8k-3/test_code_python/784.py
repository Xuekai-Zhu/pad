def solution():
    """The county fair was hosting a pumpkin contest to see who could grow the biggest pumpkin in pounds.  Brad entered his pumpkin with a weight of 54 pounds.  Jessica's was half the weight of Brad's.  Betty's pumpkin weight 4 times the amount of Jessica's pumpkin.  What is the difference between the heaviest and lightest pumpkin in pounds?"""
    # Define the weights of Brad's, Jessica's, and Betty's pumpkins
    brad_weight = 54
    jessica_weight = brad_weight / 2
    betty_weight = jessica_weight * 4

    # Calculate the heaviest and lightest pumpkins
    heaviest = max(brad_weight, jessica_weight, betty_weight)
    lightest = min(brad_weight, jessica_weight, betty_weight)

    # Calculate the difference between the heaviest and lightest pumpkins
    difference = heaviest - lightest

    # Display the difference between the heaviest and lightest pumpkins
    result = difference
    return result

print(solution())