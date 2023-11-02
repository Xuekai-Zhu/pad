def solution():
    
    first_floor_rooms = 3
    second_floor_rooms = 3
    third_floor_rooms = 3
    first_floor_price = 15
    second_floor_price = 20
    third_floor_price = 2 * first_floor_price
    total_earnings = (first_floor_price * first_floor_rooms) + (second_floor_price * second_floor_rooms) + (
            third_floor_price * 2)
    result = total_earnings
    return result

print(solution())