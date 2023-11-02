def solution():
    # Calculate the number of people who arrived before the start of the concert
    before_concert = (3/4) * 900

    # Calculate the number of people who did not arrive before the concert
    remaining = 900 - before_concert

    # Calculate the number of people who arrived after the first song
    after_first_song = (5/9) * remaining

    # Calculate the number of people who did not go to the concert
    did_not_go = remaining - after_first_song - 80

    result = did_not_go
    return result

print(solution())