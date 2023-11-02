def solution():
     cupboard_flour = 200
     counter_flour = 100
     pantry_flour = 100
     flour_required = 200
     total_flour = cupboard_flour + counter_flour + pantry_flour
     total_loaves = total_flour // flour_required
     result = total_loaves
     return result

print(solution())