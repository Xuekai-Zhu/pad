def solution():
     times_in_tall_mirror_room = 3
     times_in_wide_mirror_room = 5
     reflections_in_tall_mirror_room = 10
     reflections_in_wide_mirror_room = 5
     total_reflections = (times_in_tall_mirror_room * reflections_in_tall_mirror_room) + (times_in_wide_mirror_room * reflections_in_wide_mirror_room)
     result = total_reflections
     return result

print(solution())