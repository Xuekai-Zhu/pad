def solution():
     total_tires = 20
     initial_cars = 4
     new_cars = 6
     customers_that_didnt_want_tires_changed = total_tires - (initial_cars + new_cars)
     result = customers_that_didnt_want_tires_changed
     return result

print(solution())