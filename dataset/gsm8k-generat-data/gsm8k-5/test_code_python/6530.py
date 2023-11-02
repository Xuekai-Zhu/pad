def solution():
    papers_bought = 20  # Charles bought 20 papers
    papers_left = 2  # Charles has 2 papers left
    pictures_drawn_today = 6  # Charles drew 6 pictures today
    pictures_drawn_yesterday = 6  # Charles drew 6 pictures yesterday before going to work

    # Calculate the total number of pictures Charles drew before coming back from work
    total_pictures_before_work = pictures_drawn_today + pictures_drawn_yesterday

    # Calculate the number of pictures Charles drew after coming back from work
    pictures_drawn_after_work = papers_bought - total_pictures_before_work - papers_left
    result = pictures_drawn_after_work
    return result

print(solution())