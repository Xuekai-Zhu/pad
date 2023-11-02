def solution():
    stamps_needed = 52
    less_than_5_pounds = 6
    more_than_5_pounds = stamps_needed - (less_than_5_pounds * 2)
    total_envelopes = less_than_5_pounds + more_than_5_pounds
    result = total_envelopes
    return result

print(solution())