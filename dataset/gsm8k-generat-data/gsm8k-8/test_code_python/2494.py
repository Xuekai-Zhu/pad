def solution():
    # Define the starting rock counts
    sydney_rocks = 837
    conner_rocks = 723

    # Calculate the rock counts after day one
    sydney_rocks += 4
    conner_rocks += 8 * 4

    # Calculate the rock counts after day two
    conner_rocks += 123

    # Calculate how many Conner needs to collect on day three to tie Sydney
    conner_day_three = (sydney_rocks * 2) - conner_rocks
    result = conner_day_three
    return result

print(solution())