def solution():
     guests = 90
     cans = 50
     bottles_sparkling_water = 50
     bottles_juice = 50
     guests_soda = guests / 2
     guests_sparkling_water = guests / 3
     guests_juice = 4 * (bottles_juice / 5)
     recyclable_cans_and_bottles = cans + bottles_sparkling_water + guests_juice
     result = recyclable_cans_and_bottles
 
     return result

print(solution())