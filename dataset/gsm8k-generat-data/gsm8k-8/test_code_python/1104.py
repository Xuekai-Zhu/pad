def solution():
    # Calculate the number of people who arrived before the start of the concert
    before_start = 900 * (3/4)

    # Calculate the number of people who did not arrive before the start of the concert
    after_start = 900 - before_start

    # Calculate the number of people who arrived after the first song
    after_first_song = after_start * (5/9)

    # Calculate the number of people who did not go to the concert
    did_not_go = after_start - (after_first_song + 80)

    result = did_not_go
    return result

print(solution())