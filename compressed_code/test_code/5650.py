def solution():
    
    room_width = 20
    room_length = 20
    room_height = 8
    door1_width = 3
    door1_height = 7
    window_width = 6
    window_height = 4
    door2_width = 5
    door2_height = 7

    area1 = room_width * room_height  
    area2 = room_length * room_height  
    area3 = room_width * room_height  
    area4 = room_length * room_height  

    area1 -= door1_width * door1_height  
    area2 -= window_width * window_height  
    area3 -= door2_width * door2_height  

    total_area = area1 + area2 + area3 + area4
    result = total_area
    return result

print(solution())