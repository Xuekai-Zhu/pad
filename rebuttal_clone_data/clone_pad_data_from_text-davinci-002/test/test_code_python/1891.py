def solution():
     adult_ticket_price = 6
     child_ticket_price = 4
     total_seats = 250
     seats_filled = 188
     children_in_theatre = seats_filled
     adults_in_theatre = total_seats - children_in_theatre
     total_revenue = (adult_ticket_price * adults_in_theatre) + (child_ticket_price * children_in_theatre)
     result = total_revenue
     return result

print(solution())