def solution():
    # Calculate the number of seats in each carriage after accommodating 10 more passengers
    seats_per_carriage = 25 + 10  

    # Calculate the total number of passengers that can fit in each train 
    total_passengers_per_train = seats_per_carriage * 4  

    # Calculate the total number of passengers that can fill up 3 trains
    total_passengers_3_trains = total_passengers_per_train * 3  

    result = total_passengers_3_trains
    return result

print(solution())