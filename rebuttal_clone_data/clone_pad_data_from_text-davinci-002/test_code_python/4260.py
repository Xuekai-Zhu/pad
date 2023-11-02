def solution():
     num_guests_bridgette = 84
     num_guests_alex = num_guests_bridgette * 2/3
     num_plates = num_guests_bridgette + num_guests_alex + 10
     spears_per_plate = 8
     total_spears = num_plates * spears_per_plate
     result = total_spears
     return result

print(solution())