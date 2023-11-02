def solution():
    """ Apple High School is holding graduation in their Fine Arts Center this year which has space for 6000 people.
        After accounting for 950 seats for graduates and 300 seats for faculty attending, how many tickets would each graduate receive to give to their friends and family if the tickets are split equally?"""
    total_seats = 6000
    seats_for_graduates = 950
    seats_for_faculty = 300
    seats_for_guests = total_seats - seats_for_graduates - seats_for_faculty
    number_of_graduates = 1
    number_of_guests_per_graduate = seats_for_guests / number_of_graduates
    result = number_of_guests_per_graduate
    return result

print(solution())