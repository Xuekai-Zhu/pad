def solution():
    # Calculate the total number of pages turned in by all students
    total_pages = (5*2) + (5*3) + (5*1)  # first 5 students turned in 2-page essays, next 5 students turned in 3-page essays, last 5 students turned in 1-page essays
    # Calculate the average page count per essay
    avg_pages = total_pages / 15
    result = avg_pages
    return result

print(solution())