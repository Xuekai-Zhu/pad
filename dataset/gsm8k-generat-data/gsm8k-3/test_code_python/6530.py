def solution():
    """Charles bought 20 papers to draw. Today Charles drew 6 pictures. Yesterday he drew 6 pictures before going to work and some pictures when he came back. How many pictures did Charles draw when he came back from work knowing that he has 2 papers left?"""
    # Define the total number of papers Charles has
    total_papers = 20

    # Define the number of pictures Charles drew today and yesterday
    today_pictures = 6
    yesterday_pictures = 6

    # Calculate the number of papers Charles used for today and yesterday's pictures
    used_papers = today_pictures + yesterday_pictures

    # Calculate the number of papers Charles has left for the remaining pictures
    remaining_papers = total_papers - used_papers

    # Calculate the number of pictures Charles drew when he came back from work
    back_pictures = remaining_papers - 2

    # Display the number of pictures Charles drew when he came back from work
    result = back_pictures
    return result

print(solution())