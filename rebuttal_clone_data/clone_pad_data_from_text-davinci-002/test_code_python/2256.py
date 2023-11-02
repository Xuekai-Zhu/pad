def solution():
    time_at_carnival = 4 * 60
    roller_coaster_wait = 30 + 2
    tilt_a_whirl_wait = 60 + 4
    giant_slide_wait = 15 + 3
    time_ spent_on_roller_coaster = 4 * roller_coaster_wait
    time_spent_on_tilt_a_whirl = tilt_a_whirl_wait
    time_left = time_at_carnival - (time_spent_on_roller_coaster + time_spent_on_tilt_a_whirl)
    rides_on_giant_slide = time_left / giant_slide_wait
    result = rides_on_giant_slide
    return result

print(solution())