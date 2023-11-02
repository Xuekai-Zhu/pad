def solution():
     cars_produced = 5650000
     first_supplier = 1000000
     second_supplier = first_supplier + 500000
     third_supplier = first_supplier + second_supplier
     fourth_and_fifth_supplier = (cars_produced - (first_supplier + second_supplier + third_supplier)) / 2
     result = fourth_and_fifth_supplier
     return result

print(solution())