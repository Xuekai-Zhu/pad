def solution():
    """Charles bought 20 papers to draw. Today Charles drew 6 pictures. Yesterday he drew 6 pictures before going to work and some pictures when he came back. How many pictures did Charles draw when he came back from work knowing that he has 2 papers left?"""
    # Define the initial number of papers and the number of pictures drawn today and yesterday
    papers = 20
    today = 6
    yesterday = 6

    # Calculate the number of papers used so far
    used_papers = today + yesterday

    # Calculate the remaining papers 
    remaining_papers = papers - used_papers

    # Calculate the number of pictures drawn after work
    after_work = remaining_papers - 2

    # Return the result
    result = after_work
    return result

print(solution())