def solution():
    total_miles = 195
    katarina_miles = 51
    remaining_miles = total_miles - katarina_miles

    # Divide the remaining miles equally among the three runners
    harriet_miles = remaining_miles / 3
    result = harriet_miles
    return result

print(solution())