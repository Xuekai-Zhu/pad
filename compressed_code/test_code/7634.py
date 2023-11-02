def solution():
    
    mural_width = 20
    mural_height = 15
    square_feet = mural_width * mural_height
    time_per_square_foot = 20  
    time_per_hour = 60  
    time_taken = square_feet * time_per_square_foot
    hourly_rate = 150
    amount_charged = (time_taken / time_per_hour) * hourly_rate
    result = amount_charged
    return result

print(solution())