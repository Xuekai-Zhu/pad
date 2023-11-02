def solution():
     square_side = 2
     triangle_height = 2
     triangle_width = 2
     triangle_area = 0.5 * triangle_height * triangle_width
     square_area = square_side * square_side
     num_triangles = square_area / triangle_area
     result = num_triangles
     return result

print(solution())