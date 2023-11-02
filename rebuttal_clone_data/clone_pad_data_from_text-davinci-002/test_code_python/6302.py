def solution():
     total_cars = 125
     regular_cars = total_cars * 0.64
     trucks = total_cars * 0.08
     convertibles = total_cars - (regular_cars + trucks)
     result = convertibles
     return result

print(solution())