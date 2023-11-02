def solution():
    cars_planned = 200  # The factory was planning to produce 200 cars
    cars_shortage = 50  # Production was decreased by 50 cars due to metal shortages
    cars_produced = (cars_planned - cars_shortage) * 0.5  # Production was cut by 50% due to a pandemic
    doors_produced = cars_produced * 5  # Each car has 5 doors

    result = doors_produced
    return result

print(solution())