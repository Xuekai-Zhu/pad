def solution():
    wings_eaten = 64
    minutes = 8
    alan_wings_per_minute = 5
    kevin_wings_per_minute = wings_eaten / minutes
    difference = kevin_wings_per_minute - alan_wings_per_minute
    result = difference
    return result

print(solution())