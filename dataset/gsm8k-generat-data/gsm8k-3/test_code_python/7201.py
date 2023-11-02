def solution():
    """In one day, 200 people visit The Metropolitan Museum of Art in New York City. Half of the visitors are residents of New York City. Of the NYC residents, 30% are college students. If the cost of a college student ticket is $4, how much money does the museum get from college students that are residents of NYC?"""
    # Define the number of visitors and the proportion of NYC residents and college students
    num_visitors = 200
    nyc_ratio = 0.5
    college_ratio = 0.3

    # Calculate the number of NYC residents and college students
    nyc_residents = num_visitors * nyc_ratio
    college_students = nyc_residents * college_ratio

    # Calculate the total revenue from college students
    revenue = college_students * 4

    # Display the total revenue
    result = revenue
    return result

print(solution())