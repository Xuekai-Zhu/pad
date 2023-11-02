def solution():
    # Calculate the total number of hours Keenan needs to finish her essay
    remaining_words = 1200 - (400*2)  # subtract the first two hours' output from the total word-count
    remaining_hours = remaining_words / 200  # divide the remaining words by the hourly rate after the first 2 hours
    total_hours = remaining_hours + 2  # account for the first 2 hours of writing 

    result = total_hours
    return result

print(solution())