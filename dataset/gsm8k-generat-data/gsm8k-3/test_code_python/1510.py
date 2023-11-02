def solution():
    """Ben's hockey team is 60% boys and the rest are girls. Half the girls are juniors and the other half are seniors. If the team has 50 players, how many junior girls are there?"""
    # Define the percentage of boys on the team
    BOYS_PERCENTAGE = 60

    # Calculate the number of boys on the team
    boys = int((BOYS_PERCENTAGE / 100) * 50)

    # Calculate the number of girls on the team
    girls = 50 - boys

    # Calculate the number of junior girls
    junior_girls = girls // 2

    # Display the number of junior girls
    result = junior_girls
    return result

print(solution())