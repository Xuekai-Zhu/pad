def solution():
   """If Mr. Jones has 6 shirts for every pair of pants, and he has 40 pants, what's the total number of pieces of clothes he owns if all other factors remain the same?"""
   # Determine the number of shirts for each pair of pants
   SHIRTS_PER_PANTS = 6

   # Determine the number of shirts Mr. Jones owns
   shirts = SHIRTS_PER_PANTS * 40

   # Determine the total number of pieces of clothes Mr. Jones owns
   total = shirts + 40

   # Return the total
   result = total
   return result

print(solution())