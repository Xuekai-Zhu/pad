def solution():
     total_haircuts = 8
     haircuts_left = 2
     percent_complete = (total_haircuts - haircuts_left) / total_haircuts
     result = percent_complete * 100
     return result

print(solution())