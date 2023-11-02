def solution():
    # First, let's find out how many women are in the poll
    total_women = 100 * (39 / 65)  # We know that 35% of women are in favor of the idea, so 65% must be opposed
    women_in_poll = total_women / 0.5  # Aimee wants to get answers from 50% men and 50% women, so the number of women in the poll is half of the total number of people in the poll

    # Now, let's find out the total number of people in the poll
    total_people = women_in_poll / 0.5  # We know that 50% of the poll is women, so the other 50% must be men

    result = total_people
    return result

print(solution())