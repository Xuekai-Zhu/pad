def solution():
     flag_width = 5
     flag_height = 4
     sides_to_paint = 2
     area_to_paint = flag_width * flag_height * sides_to_paint
     paint_coverage = 4
     quarts_of_paint = area_to_paint / paint_coverage
     cost_of_paint = 2 * quarts_of_paint
     result = cost_of_paint
     
     return result

print(solution())