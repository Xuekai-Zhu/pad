def solution():
    total_visitors = 200  # 200 people visit the museum in one day
    nyc_residents = total_visitors / 2  # Half of the visitors are residents of NYC
    college_students = nyc_residents * 0.3  # 30% of NYC residents are college students
    ticket_cost = 4  # The cost of a college student ticket is $4

    # Calculate the total money collected from college student NYC residents
    total_money = college_students * ticket_cost
    result = total_money
    return result

print(solution())