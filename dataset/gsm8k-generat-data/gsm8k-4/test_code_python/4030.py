def solution():
    """In the beginning, Justine had 10 more rubber bands than Bailey but 2 fewer bands than Ylona. Bailey decided to give two bands each to Justine and Ylona so that he is left with only 8 rubber bands. How many rubber bands did Ylona have in the beginning?"""
    # Define the initial number of rubber bands for Bailey and calculate the number for Justine and Ylona
    bailey_bands = None
    justine_bands = bailey_bands + 10
    ylona_bands = justine_bands + 2

    # Update the number of rubber bands after Bailey gives 2 to Justine and Ylona
    bailey_bands -= 4
    justine_bands += 2
    ylona_bands += 2

    # Update the number of rubber bands after Bailey is left with 8
    bailey_bands += 8

    result = ylona_bands
    return result

print(solution())