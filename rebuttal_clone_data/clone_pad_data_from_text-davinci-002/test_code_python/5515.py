def solution():
    kids_waiting_swings = 3
    kids_waiting_slide = kids_waiting_swings * 2
    total_kids = kids_waiting_swings + kids_waiting_slide
    swings_time = 2
    slide_time = 15
    total_time_swings = swings_time * kids_waiting_swings
    total_time_slide = slide_time * kids_waiting_slide
    difference = total_time_swings - total_time_slide
    return difference

print(solution())