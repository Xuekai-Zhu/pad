def solution():
    # Define the number of votes for the witch cake
    witch_votes = 7

    # Calculate the number of votes for the unicorn cake
    unicorn_votes = witch_votes * 3

    # Calculate the number of votes for the dragon cake
    dragon_votes = witch_votes + 25

    # Calculate the total number of votes
    total_votes = witch_votes + unicorn_votes + dragon_votes
    result = total_votes
    return result

print(solution())