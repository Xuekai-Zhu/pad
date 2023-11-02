def solution():
    capacity = 2000
    total_people = capacity * 3 / 4
    entry_fee = 20

    # Calculate the total fees collected when the stadium was 3/4 full
    total_fees_3_4_full = total_people * entry_fee

    # Calculate the total fees that would have been collected if the stadium was full
    total_fees_full = capacity * entry_fee

    # Calculate the difference between the two
    difference = total_fees_full - total_fees_3_4_full
    result = difference
    return result

print(solution())