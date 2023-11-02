def solution():
    # Calculate the number of trains arriving in an hour
    num_trains = 60 // 5  # 60 minutes in an hour, trains come every 5 minutes

    # Calculate the total number of passengers stepping on and off the trains
    passengers_per_train = 200 + 320  # 200 passengers leave, 320 passengers board
    total_passengers = passengers_per_train * num_trains

    # Calculate the number of different passengers (i.e. unique individuals) stepping on and off the trains
    # Assuming no one takes more than one train
    different_passengers = total_passengers  
    result = different_passengers
    return result

print(solution())