def solution():
    """Johnny wrote an essay with 150 words. Madeline wrote an essay that was double in length, and Timothy wrote an essay that had 30 words more than Madeline's. If one page contains 260 words, how many pages do Johnny, Madeline, and Timothy's essays fill?"""
    # Define the lengths of the essays
    johnny_length = 150
    madeline_length = johnny_length * 2
    timothy_length = madeline_length + 30

    # Calculate the number of pages each essay fills
    johnny_pages = johnny_length / 260
    madeline_pages = madeline_length / 260
    timothy_pages = timothy_length / 260

    # Round up to the nearest integer to get the final number of pages
    johnny_pages = int(johnny_pages) + (johnny_pages % 1 > 0)
    madeline_pages = int(madeline_pages) + (madeline_pages % 1 > 0)
    timothy_pages = int(timothy_pages) + (timothy_pages % 1 > 0)

    # Return the result as a tuple
    result = (johnny_pages, madeline_pages, timothy_pages)
    return result

print(solution())