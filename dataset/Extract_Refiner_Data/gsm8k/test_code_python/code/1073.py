def solution():
    
    # Define the time it takes for each train to arrive in minutes
    train1_time = 10
    train1_stay_time = 20
    train2_time = train1_time / 2
    train2_stay_time = train1_stay_time / 4
    train3_time = train1_stay_time / 4

    # Calculate the total time it takes for all four trains to arrive at the station
    total_time = train1_time + train1_stay_time + train2_time + train3_stay_time

    # Display the total time
    result = total_time
    return result

print(solution())