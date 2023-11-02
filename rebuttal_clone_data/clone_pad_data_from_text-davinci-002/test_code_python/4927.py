def solution():
     first_tree = 1000
     second_tree = first_tree / 2
     third_tree = first_tree + 200
     average_height = (first_tree + second_tree + third_tree) / 3
     result = average_height
     return result

print(solution())