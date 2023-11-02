def solution():
     front_parking_lot = 100
     back_parking_lot = front_parking_lot * 2
     total_cars = 700
     cars_during_play = total_cars - (front_parking_lot + back_parking_lot)
     result = cars_during_play
     return result

print(solution())