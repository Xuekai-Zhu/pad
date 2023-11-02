def solution():
    
    total_tickets = 900
    before_concert = total_tickets * 0.75
    remaining_tickets = total_tickets - before_concert
    after_first_song = remaining_tickets * (5/9)
    middle_concert = 80
    not_attending = total_tickets - before_concert - after_first_song - middle_concert
    result = not_attending
    return result

print(solution())