def solution():
     total_floors = 12
     floors_with_6_apartments = total_floors / 2
     floors_with_5_apartments = total_floors - floors_with_6_apartments
     apartments_with_6_residents = floors_with_6_apartments * 6
     apartments_with_5_residents = floors_with_5_apartments * 5
     total_residents = apartments_with_6_residents + apartments_with_5_residents
     result = total_residents
     return result

print(solution())