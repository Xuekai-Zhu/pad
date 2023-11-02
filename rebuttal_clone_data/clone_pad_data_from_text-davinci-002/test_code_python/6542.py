def solution():
     bedrooms = 3
     other_rooms = bedrooms * 2
     total_rooms = bedrooms + other_rooms
     paint_per_bedroom = 2
     paint_per_other_room = 1
     total_paint_needed = (bedrooms * paint_per_bedroom) + (other_rooms * paint_per_other_room)
     paint_cans_needed = total_paint_needed / 3
     result = paint_cans_needed
     return result

print(solution())