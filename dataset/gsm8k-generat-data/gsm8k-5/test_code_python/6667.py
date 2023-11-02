def solution():
    pages_written = 6  # Rachel wrote 6 pages
    time_writing = (pages_written * 30) / 60  # Rachel spends 30 minutes per page, so calculate total time writing in hours
    time_researching = 45 / 60  # Rachel spends 45 minutes researching, so convert to hours
    time_editing = 75 / 60  # Rachel spends 75 minutes editing, so convert to hours
    total_time = time_writing + time_researching + time_editing  # Calculate total time spent on the essay
    result = total_time
    return result

print(solution())