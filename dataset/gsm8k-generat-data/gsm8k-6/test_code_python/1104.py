def solution():
    total_tickets = 900  # total number of tickets sold
    before_concert = (3/4) * total_tickets  # number of people who came before the start of the concert
    remaining_tickets = total_tickets - before_concert  # number of tickets left after those who came before the concert
    after_first_song = (5/9) * remaining_tickets  # number of people who came after the first song
    not_arrived = total_tickets - before_concert - after_first_song - 80  # number of people who did not go to the concert

    result = not_arrived
    return result

print(solution())