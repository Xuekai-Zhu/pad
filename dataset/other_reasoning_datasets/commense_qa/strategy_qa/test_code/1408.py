def solution():
    best_growing_conditions = "cool temperatures with lots of sun"
    largest_producer_state = "California"
    arid_climate_state = "Arizona"
    if best_growing_conditions not in arid_climate_state and largest_producer_state != arid_climate_state:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())