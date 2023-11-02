def solution():
    # Square feet painted on Monday
    monday = 30
  
    # Square feet painted on Tuesday
    tuesday = 2 * monday
  
    # Square feet painted on Wednesday
    wednesday = monday / 2
  
    # Total square feet painted
    total = monday + tuesday + wednesday
    result = total
    return result

print(solution())