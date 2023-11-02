def solution():
    total_miles = 195  # The runners ran a combined total of 195 miles
    katarina_miles = 51  # Katarina ran 51 miles
    miles_remaining = total_miles - katarina_miles  # Total miles - Katarina's miles = miles ran by Tomas, Tyler, and Harriet
    miles_each = miles_remaining / 3  # Divide miles remaining equally among Tomas, Tyler, and Harriet

    # Harriet ran the same distance as Tomas and Tyler
    harriet_miles = miles_each
    result = harriet_miles
    return result

print(solution())