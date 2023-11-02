def solution():
    sable_genus = "Martes"
    wolverine_genus = "Gulo"
    mustelidae_family = True
    
    # Check if sables and wolverines are from the same family
    if mustelidae_family:
        # Check if sables and wolverines are from the same genus
        if sable_genus == wolverine_genus:
            result = "yes"
        else:
            result = "no"
    else:
        result = "no"
    return result

print(solution())