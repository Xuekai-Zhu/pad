def solution():
    disneyland_paris_parks = 2
    disneyland_paris_hotels =  several
    disneyland_paris_shopping_districts = 1
    
    disney_world_parks = 4
    disney_world_waterparks = 2
    disney_world_hotels = many
    disney_world_shopping_districts = 1
    
    disneyland_paris_size = disneyland_paris_parks + disneyland_paris_hotels + disneyland_paris_shopping_districts
    disney_world_size = disney_world_parks + disney_world_waterparks + disney_world_hotels + disney_world_shopping_districts
    
    if disneyland_paris_size < disney_world_size:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())