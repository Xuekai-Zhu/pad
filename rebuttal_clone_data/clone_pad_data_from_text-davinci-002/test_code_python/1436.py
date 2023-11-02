def solution():
    Charlie_flutes = 1
    Charlie_horns = 2
    Charlie_harps = 1
     
     Carli_flutes = Charlie_flutes * 2
     Carli_horns = Charlie_horns / 2
     Carli_harps = 0
     
     total_instruments = Charlie_flutes + Charlie_horns + Charlie_harps + Carli_flutes + Carli_horns + Carli_harps
     result = total_instruments
     return result

print(solution())