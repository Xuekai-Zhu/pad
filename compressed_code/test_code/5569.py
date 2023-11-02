def solution():
    
    total_visitors = 200
    nyc_residents = total_visitors / 2
    college_students = nyc_residents * 0.3
    college_student_ticket_price = 4
    total_money = college_students * college_student_ticket_price
    result = total_money
    return result

print(solution())