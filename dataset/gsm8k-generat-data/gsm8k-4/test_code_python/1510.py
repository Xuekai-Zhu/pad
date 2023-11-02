def solution():
    """Ben's hockey team is 60% boys and the rest are girls. Half the girls are juniors and the other half are seniors. If the team has 50 players, how many junior girls are there?"""
    # Define the percentage of boys on the team
    boys_percentage = 0.6

    # Calculate the number of boys on the team
    boys = 50 * boys_percentage

    # Calculate the number of girls on the team
    girls = 50 - boys

    # Calculate the number of junior girls
    junior_girls = girls / 2

    # return the result
    result = junior_girls
    return result

print(solution())