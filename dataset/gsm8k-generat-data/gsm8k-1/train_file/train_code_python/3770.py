def solution():
    """Jenny is scraping gum off the bottom of the seats in a stadium with two sections. 
    Section A has 1 subsection with 60 seats and 3 subsections with 80 seats each. 
    Section B has 20 more seats than 3 times as many seats as Section A has total. 
    How many seats does Section B have?"""
    
    # Seats in section A
    seats_A_subsection1 = 60
    seats_A_subsection2 = 80
    seats_A_subsection3 = 80
    total_seats_A = seats_A_subsection1 + (3 * seats_A_subsection2) + (3 * seats_A_subsection3)
    
    # Seats in section B
    seats_B = (3 * total_seats_A) + 20
    
    result = seats_B
    return result

print(solution())