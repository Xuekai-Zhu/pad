def solution():
    first_floor_rooms = 3
    first_floor_price = 15

    second_floor_rooms = 3
    second_floor_price = 20

    third_floor_rooms = 3
    third_floor_price = 2 * first_floor_price  # twice as much as first floor
    third_floor_occupied_rooms = 2

    # Calculate the total earnings from the first floor rooms
    first_floor_earnings = first_floor_rooms * first_floor_price

    # Calculate the total earnings from the second floor rooms
    second_floor_earnings = second_floor_rooms * second_floor_price

    # Calculate the total earnings from the third floor rooms
    third_floor_earnings = third_floor_occupied_rooms * third_floor_price

    # Calculate the total earnings from all floors
    total_earnings = first_floor_earnings + second_floor_earnings + third_floor_earnings
    result = total_earnings
    return result

print(solution())