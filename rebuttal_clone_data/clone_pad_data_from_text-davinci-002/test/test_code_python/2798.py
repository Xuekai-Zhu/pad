def solution():
     matinee_ticket_price = 5
     evening_ticket_price = 7
     opening_night_ticket_price = 10
     matinee_customers = 32
     evening_customers = 40
     opening_night_customers = 58
     popcorn_price = 10
     half_popcorn_customers = (matinee_customers + evening_customers + opening_night_customers) / 2
     total_ticket_sales = (matinee_customers * matinee_ticket_price) + (evening_customers * evening_ticket_price) + (opening_night_customers * opening_night_ticket_price)
     total_popcorn_sales = half_popcorn_customers * popcorn_price
     total_sales = total_ticket_sales + total_popcorn_sales
     result = total_sales
     return result

print(solution())