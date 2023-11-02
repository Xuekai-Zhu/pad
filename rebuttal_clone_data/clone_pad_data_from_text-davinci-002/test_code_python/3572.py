def solution():
    minutes_to_iron_blouse = 15
    minutes_to_iron_dress = 20
    hours_to_iron_blouses = 2
    hours_to_iron_dresses = 3
    total_minutes = (hours_to_iron_blouses * 60) + (hours_to_iron_dresses * 60)
    blouses_ironed = (total_minutes / minutes_to_iron_blouse)
    dresses_ironed = (total_minutes / minutes_to_iron_dress)
    total_pieces = blouses_ironed + dresses_ironed
    result = total_pieces
    
    return result

print(solution())