def solution():
    owen_turtles = 21
    johanna_turtles = owen_turtles - 5
    
    # After 1 month, Owen has twice as many turtles as before (42) and Johanna loses half of her turtles (8)
    owen_turtles += 42
    johanna_turtles /= 2
    owen_turtles += johanna_turtles
    
    result = owen_turtles
    return result

print(solution())