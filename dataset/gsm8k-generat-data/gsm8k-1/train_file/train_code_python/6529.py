def solution():
    """Charles bought 20 papers to draw. Today Charles drew 6 pictures. Yesterday he drew 6 pictures before going to work and some pictures when he came back. How many pictures did Charles draw when he came back from work knowing that he has 2 papers left?"""
    total_papers = 20
    papers_left = 2
    pictures_today = 6
    pictures_yesterday = 6
    pictures_left = total_papers - pictures_today - pictures_yesterday - papers_left
    result = pictures_left
    return result

print(solution())