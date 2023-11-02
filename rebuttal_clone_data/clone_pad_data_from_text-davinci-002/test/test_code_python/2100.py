def solution():
    yield_good_soil = 400
    yield_clay_soil = yield_good_soil / 2
    acres_good_soil = 40
    acres_clay_soil = 20
    total_acres = acres_good_soil + acres_clay_soil
    total_yield = (acres_good_soil * yield_good_soil) + (acres_clay_soil * yield_clay_soil)
    result = total_yield
    
    return result

print(solution())