def solution():
    """Leo has to write a 400-word story for his literature class. 10 words fit on each line of his notebook and 20 lines fit on each page. Lucas has filled one and a half pages. How many words does he have left to write?"""
    # Define the number of words that can fit on one page
    words_per_page = 10 * 20

    # Define the number of pages Lucas has already filled
    filled_pages = 1.5

    # Calculate the total number of words Lucas has written so far
    words_so_far = filled_pages * words_per_page

    # Calculate the number of words Lucas has left to write
    words_left = 400 - words_so_far

    # Return the result
    result = words_left
    return result

print(solution())