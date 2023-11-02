def solution():
   # Calculate the height of the first 100 floors
   first_100_floors = 100 * 16.5

   # Subtract the height of the first 100 floors from the total height of Taipei 101
   height_101st_floor = 1673 - first_100_floors
   result = height_101st_floor
   return result

print(solution())