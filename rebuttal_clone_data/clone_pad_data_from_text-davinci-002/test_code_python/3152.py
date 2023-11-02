def solution():
     cucumber_sandwiches = 10
     egg_sandwiches = 8
     triangles_per_cucumber_sandwich = 4
     rectangles_per_egg_sandwich = 2
     total_triangles_consumed = 28
     total_rectangles_consumed = 12
     total_slices_of_bread_consumed = (total_triangles_consumed / triangles_per_cucumber_sandwich) + (total_rectangles_consumed / rectangles_per_egg_sandwich)
     result = total_slices_of_bread_consumed
     return result

print(solution())