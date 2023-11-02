def solution():
     student_ticket_price = 6
     adult_ticket_price = 8
     num_student_tickets_sold = 20
     num_adult_tickets_sold = 12
     student_ticket_sales = num_student_tickets_sold * student_ticket_price
     adult_ticket_sales = num_adult_tickets_sold * adult_ticket_price
     total_sales = student_ticket_sales + adult_ticket_sales
     result = total_sales
 
     return result

print(solution())