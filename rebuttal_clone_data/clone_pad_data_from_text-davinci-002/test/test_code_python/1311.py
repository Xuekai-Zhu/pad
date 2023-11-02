def solution():
     mural_area = 20 * 15
     minutes_per_square_foot = 20
     minutes_to_paint_mural = mural_area * minutes_per_square_foot
     hours_to_paint_mural = minutes_to_paint_mural / 60
     cost_to_paint_mural = hours_to_paint_mural * 150
     result = cost_to_paint_mural
 
     return result

print(solution())