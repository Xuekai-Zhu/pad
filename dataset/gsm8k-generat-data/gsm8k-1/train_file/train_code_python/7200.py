def solution():
    """In one day, 200 people visit The Metropolitan Museum of Art in New York City. Half of the visitors are residents of New York City. Of the NYC residents, 30% are college students. If the cost of a college student ticket is $4, how much money does the museum get from college students that are residents of NYC?"""
    total_visitors = 200
    nyc_residents = total_visitors / 2
    college_students = nyc_residents * 0.3
    ticket_price = 4
    money_made = college_students * ticket_price
    result = money_made
    return result

print(solution())