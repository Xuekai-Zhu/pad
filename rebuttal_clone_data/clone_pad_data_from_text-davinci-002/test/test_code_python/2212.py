def solution():
     classes = 6
     folders = classes
     pencils = classes * 3
     erasers = pencils / 6
     paint_sets = 1
     cost_of_folders = folders * 6
     cost_of_pencils = pencils * 2
     cost_of_erasers = erasers * 1
     cost_of_paint_sets = 80 - (cost_of_folders + cost_of_pencils + cost_of_erasers)
     result = cost_of_paint_sets
     return result

print(solution())