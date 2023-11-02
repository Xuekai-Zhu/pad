def solution():
    cartons_processed = 400
    cartons_delivered = cartons_processed / 4
    cartons_returned = cartons_delivered / 60
    total_cartons = cartons_processed - cartons_returned
    result = total_cartons
    return result

print(solution())