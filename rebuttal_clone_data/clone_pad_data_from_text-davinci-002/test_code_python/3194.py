def solution():
     total_guests = 1000
     married_guests = total_guests * 0.3
     child_guests = total_guests * 0.2
     result = married_guests - child_guests
     return result

print(solution())