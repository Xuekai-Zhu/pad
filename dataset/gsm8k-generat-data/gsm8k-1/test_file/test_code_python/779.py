def solution():
    """Bob had 7 fish in his ornamental fish pond. 3 were orange, and 4 were white. He decided he wanted to get some more, so he went to the pet store. He had a sales assistant at the pet shop dip out 17 fish out of a mixed tank of both white and orange fish. When he got them home and added them to his pond, he found that he now had twice as many orange fish as white fish. How many white fish did Bob buy at the store?"""
    
    # Initial fish in pond
    initial_orange = 3
    initial_white = 4
    # Fish Bob bought
    total_bought = 17
    # Calculate current number of orange fish
    current_orange = 2 * initial_white
    # Calculate current number of total fish
    current_total = initial_orange + current_orange + initial_white + (total_bought - current_orange)
    # Calculate current number of white fish
    current_white = current_total - initial_orange - current_orange
    
    result = current_white
    return result

print(solution())