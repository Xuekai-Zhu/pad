def solution():
     total_tickets = 400
     share_fraction = 3/4
     friend_one_tickets = total_tickets * share_fraction * (4/15)
     friend_two_tickets = total_tickets * share_fraction * (11/15)
     result = friend_two_tickets
 
     return result

print(solution())