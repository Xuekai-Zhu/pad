def solution():
    # Calculate the total number of drawings on the first five pages
    total_drawings = 5 + (5+5) + (5+5+5) + (5+5+5+5) + (5+5+5+5+5)  # number of drawings on each page increases by 5 after every page
    result = total_drawings
    return result

print(solution())