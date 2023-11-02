def solution():
    total_tickets_sold = 900
    people_before_concert = total_tickets_sold * (3/4)
    people_after_first_song = people_before_concert * (5/9)
    people_during_middle = 80
    people_who_didnt_go = total_tickets_sold - (people_before_concert + people_after_first_song + people_during_middle)
    result = people_who_didnt_go
    return result

print(solution())