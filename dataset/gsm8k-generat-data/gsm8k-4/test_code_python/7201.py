def solution():
    """In one day, 200 people visit The Metropolitan Museum of Art in New York City. Half of the visitors are residents of New York City. Of the NYC residents, 30% are college students. If the cost of a college student ticket is $4, how much money does the museum get from college students that are residents of NYC?"""
    # Define the total number of visitors and NYC residents
    total_visitors = 200
    nyc_residents = total_visitors / 2

    # Calculate the number of college students in NYC
    college_students = nyc_residents * 0.3

    # Calculate the money earned from college students
    college_student_money = college_students * 4

    # return result
    result = college_student_money
    return result

print(solution())