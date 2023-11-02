def solution():
    num_papers = 20
    num_drawn_today = 6
    num_drawn_yesterday = 6
    num_papers_left = 2

    # Calculate the total number of pictures that Charles drew so far
    total_drawn = num_drawn_today + num_drawn_yesterday

    # Calculate the number of papers used for the pictures already drawn
    papers_used = total_drawn

    # Calculate the number of papers left
    papers_left = num_papers - papers_used

    # Calculate the number of pictures Charles drew when he came back from work
    num_drawn_after_work = papers_left - num_papers_left

    result = num_drawn_after_work
    return result

print(solution())