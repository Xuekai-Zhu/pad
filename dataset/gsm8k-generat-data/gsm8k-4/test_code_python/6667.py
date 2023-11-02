def solution():
    """Rachel is writing an essay. She writes 1 page every 30 minutes. She spends 45 minutes researching the topic. She writes a total of 6 pages. Then she spends 75 minutes editing her essay. Altogether, how many hours did she spend completing the essay?"""
    # Calculate the time spent writing the essay
    time_writing = 6 * 30

    # Calculate the total time spent on the essay
    total_time = time_writing + 45 + 75

    # Convert the total time to hours
    total_hours = total_time / 60

    # Return the result
    result = total_hours
    return result

print(solution())