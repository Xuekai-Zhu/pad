def solution():
    """Charles bought 20 papers to draw. Today Charles drew 6 pictures. Yesterday he drew 6 pictures before going to work and some pictures when he came back. How many pictures did Charles draw when he came back from work knowing that he has 2 papers left?"""
    total_papers = 20
    today_drawn = 6
    yesterday_drawn = 6
    remaining_papers = 2
    total_drawn = today_drawn + yesterday_drawn
    drawn_after_work = total_drawn - remaining_papers
    result = drawn_after_work
    return result

print(solution())