def solution():
    tall_mirror_room = 3  # number of times they passed through the room with tall mirrors
    wide_mirror_room = 5  # number of times they passed through the room with wide mirrors

    sarah_tall_mirror_reflections = 10 * tall_mirror_room
    sarah_wide_mirror_reflections = 5 * wide_mirror_room
    sarah_total_reflections = sarah_tall_mirror_reflections + sarah_wide_mirror_reflections

    ellie_tall_mirror_reflections = 6 * tall_mirror_room
    ellie_wide_mirror_reflections = 3 * wide_mirror_room
    ellie_total_reflections = ellie_tall_mirror_reflections + ellie_wide_mirror_reflections

    total_reflections = sarah_total_reflections + ellie_total_reflections

    return total_reflections

print(solution())