def solution():
     cartons_recieved = 50
     jars_per_carton = 20
     cartons_damaged = 20 + 5
     jars_damaged = 3 * 5 + 1 * 20
     jars_good = cartons_recieved * jars_per_carton - cartons_damaged
     result = jars_good
     return result

print(solution())