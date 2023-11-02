def solution():
     males = 15
     females = 10
     total_attendees = males + females
     drinks_per_attendee = 2
     total_drinks = total_attendees * drinks_per_attendee
     cans_per_box = 8
     boxes_bought = total_drinks / cans_per_box
     price_per_box = 5
     total_spent = boxes_bought * price_per_box
     result = total_spent 
     return result

print(solution())