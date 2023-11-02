def solution():
    """Last night Rick killed ten wolves and 15 cougars while hunting. Today Rick killed three times as many wolves as cougars and three fewer cougars than the previous night. How many animals did Rick kill?"""
    
    wolves_night1 = 10
    cougars_night1 = 15
    
    cougars_night2 = cougars_night1 - 3
    wolves_night2 = 3 * cougars_night2
    
    total_animals = wolves_night1 + cougars_night1 + cougars_night2 + wolves_night2
    result = total_animals
    
    return result

print(solution())