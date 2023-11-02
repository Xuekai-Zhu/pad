def solution():
    """Colin ran his first mile in 6 minutes. He ran his next two miles in 5 minutes each and finished his 4th mile in 4 minutes. What was the average time it took him to run a mile?"""
    # Define the time taken to run each mile
    mile1 = 6
    mile2 = 5
    mile3 = 5
    mile4 = 4

    # Calculate the total time taken to run all 4 miles
    total_time = mile1 + mile2 + mile3 + mile4

    # Calculate the average time taken to run a mile
    average_time = total_time / 4

    result = average_time
    return result

print(solution())