def solution():
     art_supplies = 90000
     canvases = 40000
     paints = canvases / 2
     easel = 15000
     paintbrushes = art_supplies - canvases - paints - easel
     result = paintbrushes
     return result

print(solution())