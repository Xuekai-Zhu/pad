def solution():
     passengers = 80
     men = 30
     women = passengers - men
     children = passengers - men - women
     result = children
     return result

print(solution())