def solution():
    """In the baking contest, three times as many people voted for the unicorn cake compared to the witch cake, and the number of votes for the dragon cake was 25 more than the number of votes for the witch cake. If 7 people voted for the witch cake, how many votes were cast total?"""
    # Define the number of votes for the witch cake
    witch_votes = 7

    # Calculate the number of votes for the unicorn cake
    unicorn_votes = 3 * witch_votes

    # Calculate the number of votes for the dragon cake
    dragon_votes = witch_votes + 25

    # Calculate the total number of votes
    total_votes = witch_votes + unicorn_votes + dragon_votes

    # Display the total number of votes
    result = total_votes
    return result

print(solution())