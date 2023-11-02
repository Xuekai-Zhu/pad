def solution():
    # Calculate the total number of seats in Section A
    seats_section_a = (1 * 60) + (3 * 80)  
    # Calculate three subsections with 80 seats each

    # Calculate how many seats Section B has
    seats_section_b = (3 * seats_section_a) + 20  # Section B has 20 seats more than 3 times Section A's total seats

    result = seats_section_b
    return result

print(solution())