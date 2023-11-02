def solution():
     ink_used = ((4 * 4) * 2) + ((6 * 2) * 2)
     ink_available = (3 * (4 * 4))
     ink_left = ink_available - ink_used
     Percentage_left = (ink_left / ink_available) * 100
     result = Percentage_left
     return result

print(solution())