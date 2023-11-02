def solution():
     loads_on_wednesday = 6
     loads_on_thursday = loads_on_wednesday * 2
     loads_on_friday = loads_on_thursday / 2
     loads_on_saturday = loads_on_wednesday / 3
     total_loads = loads_on_wednesday + loads_on_thursday + loads_on_friday + loads_on_saturday
     result = total_loads
     return result

print(solution())