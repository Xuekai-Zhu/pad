def solution():
    """Jenny is scraping gum off the bottom of the seats in a stadium with two sections. Section A has 1 subsection with 60 seats and 3 subsections with 80 seats each. Section B has 20 more seats than 3 times as many seats as Section A has total. How many seats does Section B have?"""
    # Calculate the number of seats in Section A
    section_a_seats = 60 + (3 * 80)

    # Calculate the number of seats in Section B
    section_b_seats = (3 * section_a_seats) + 20

    # Display the number of seats in Section B
    result = section_b_seats
    return result

print(solution())