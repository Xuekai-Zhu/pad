def solution():
    total_pictures = 20  # papers bought
    pictures_drawn_yesterday = 6
    pictures_drawn_today = 6
    papers_left = 2
    pictures_drawn_when_back = total_pictures - (pictures_drawn_yesterday + pictures_drawn_today + papers_left)  # remaining papers were used to draw pictures when back from work
    result = pictures_drawn_when_back
    return result

print(solution())