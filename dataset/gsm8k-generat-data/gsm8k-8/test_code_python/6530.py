def solution():
    total_drawings = 20
    drawings_today = 6
    drawings_yesterday = 6
    papers_left = 2

    # Subtract the drawings Charles made today and yesterday from the total
    remaining_drawings = total_drawings - drawings_today - drawings_yesterday

    # Subtract the number of papers left from the remaining drawings to find how many drawings Charles made when he came back from work
    drawings_after_work = remaining_drawings - papers_left
    result = drawings_after_work
    return result

print(solution())