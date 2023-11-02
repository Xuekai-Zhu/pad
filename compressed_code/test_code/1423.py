def solution():
    

    hostel_nights = 3
    hostel_price = 15
    cabin_nights = 2
    cabin_price = 45 / 3  
    total_lodging_cost = (hostel_nights * hostel_price) + (cabin_nights * cabin_price)
    result = total_lodging_cost
    return result

print(solution())