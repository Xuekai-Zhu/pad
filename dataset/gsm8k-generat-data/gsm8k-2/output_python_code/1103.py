def solution():
    """Nine hundred tickets were sold to a concert. Three-fourths of those who bought the ticket came before the start of the concert. Five-ninths of the remaining came few minutes after the first song. Eighty people arrived during the middle part of the concert while the rest did not go. How many of those who bought the tickets did not go?"""
    total_tickets = 900
    before_concert = total_tickets * 0.75
    remaining_tickets = total_tickets - before_concert
    after_first_song = remaining_tickets * (5/9)
    middle_concert = 80
    not_attending = total_tickets - before_concert - after_first_song - middle_concert
    result = not_attending
    return result

print(solution())