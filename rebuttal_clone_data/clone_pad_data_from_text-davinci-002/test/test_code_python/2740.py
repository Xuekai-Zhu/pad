def solution():
     num_triangles = 12
     num_squares = 8
     num_pentagons = 4
    
     lines_triangles = num_triangles * 3
     lines_squares = num_squares * 4
     lines_pentagons = num_pentagons * 5
    
     total_lines = lines_triangles + lines_squares + lines_pentagons
     result = total_lines
     return result

print(solution())