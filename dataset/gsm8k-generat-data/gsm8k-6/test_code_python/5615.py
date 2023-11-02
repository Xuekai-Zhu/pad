def solution():
    # Calculate the number of phones Kevin and his coworker need to repair
    total_phones = 15 + 6  # Kevin starts with 15 phones and the client drops off 6 more
    remaining_phones = total_phones - 3  # Kevin repairs 3 phones by the afternoon
    phones_to_be_repaired_by_both = remaining_phones / 2  # Kevin's coworker offers to help him and fix half of the phones remaining
    phones_each = phones_to_be_repaired_by_both + 3  # Kevin already fixed 3 phones
    result = phones_each
    return result

print(solution())