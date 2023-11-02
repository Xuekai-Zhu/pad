def solution():
     notebooks_before = 4
     notebooks_ordered = 6
     notebooks_lost = 2
     notebooks_now = notebooks_before + notebooks_ordered - notebooks_lost
     result = notebooks_now
     return result

print(solution())