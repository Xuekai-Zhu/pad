def solution():
     initial_tickets = 11
     friends = 0
     while initial_tickets > 3:
         friends += 1
         initial_tickets -= 2
     result = friends
     return result

print(solution())