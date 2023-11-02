def solution():
     lot_length = 400
     lot_width = 500
     usable_percentage = 80
     usable_area = lot_length * lot_width * (usable_percentage / 100)
     parking_space = 10
     total_cars = usable_area / parking_space
     result = total_cars
     return result

print(solution())