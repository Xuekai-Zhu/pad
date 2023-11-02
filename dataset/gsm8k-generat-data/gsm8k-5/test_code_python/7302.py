def solution():
    room_width = 20
    room_length = 20
    room_height = 8

    # Calculate the area of the first wall
    first_wall_area = room_height * room_width
    # Subtract the area of the doorway on the first wall
    first_door_area = 3 * 7
    first_wall_area -= first_door_area

    # Calculate the area of the second wall
    second_wall_area = room_height * room_length
    # Subtract the area of the window on the second wall
    second_window_area = 6 * 4
    second_wall_area -= second_window_area

    # Calculate the area of the third wall
    third_wall_area = room_height * room_width
    # Subtract the area of the doorway to the walk-in closet on the third wall
    closet_door_area = 5 * 7
    third_wall_area -= closet_door_area

    # Calculate the area of the fourth wall (which is solid)
    fourth_wall_area = room_height * room_length

    # Calculate the total area of wall space Linda needs to paint
    total_wall_area = 2 * first_wall_area + 2 * second_wall_area + third_wall_area + fourth_wall_area
    result = total_wall_area
    return result

print(solution())