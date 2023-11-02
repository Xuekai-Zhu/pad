def solution():
    # Calculate how many stamps were used for envelopes less than 5 pounds
    stamps_less_5lbs = 6 * 2

    # Calculate how many stamps were used for envelopes weighing more than 5 pounds
    stamps_more_5lbs = 52 - stamps_less_5lbs

    # Calculate how many envelopes were needed for stamps_more_5lbs
    envelopes_more_5lbs = stamps_more_5lbs / 5

    # Calculate the total number of envelopes needed
    total_envelopes = 6 + envelopes_more_5lbs
    result = total_envelopes
    return result

print(solution())