def solution():
    
    first_train_arrival_time = 10
    first_train_stay_in_station = 20
    second_train_arrival_time = 0.5 * first_train_arrival_time
    second_train_stay_in_station = (1/4) * second_train_arrival_time
    third_train_arrival_time = (1/4) * first_train_arrival_time
    total_time = first_train_stay_in_station + second_train_stay_in_station + third_train_arrival_time
    result = total_time
    return result

print(solution())