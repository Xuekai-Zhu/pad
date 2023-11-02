def solution():
    total_visitors = 200
    nyc_residents = total_visitors / 2
    college_students = nyc_residents * 0.3
    ticket_price = 4.0
    total_income = college_students * ticket_price
    result = total_income
    return result

print(solution())