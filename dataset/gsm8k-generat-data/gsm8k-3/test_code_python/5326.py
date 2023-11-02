def solution():
    """Colin ran his first mile in 6 minutes. He ran his next two miles in 5 minutes each and finished his 4th mile in 4 minutes. What was the average time it took him to run a mile?"""
    
    # Define the time taken for each mile
    mile_1 = 6
    mile_2 = 5
    mile_3 = 5
    mile_4 = 4
    
    # Calculate the total time taken for all 4 miles
    total_time = mile_1 + mile_2 + mile_3 + mile_4
    
    # Calculate the average time per mile
    average_time = total_time/4
    
    # Display the average time per mile
    result = average_time
    return result

print(solution())