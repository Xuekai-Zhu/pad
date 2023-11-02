def solution():
    num_less_than_five_pounds = 6
    num_stamps_less_than_five_pounds = num_less_than_five_pounds * 2
    total_num_stamps_needed = 52

    # Calculate the number of stamps needed for envelopes weighing more than 5 pounds
    num_stamps_more_than_five_pounds = total_num_stamps_needed - num_stamps_less_than_five_pounds

    # Calculate the number of envelopes weighing more than 5 pounds
    num_more_than_five_pounds = num_stamps_more_than_five_pounds / 5

    # Calculate the total number of envelopes needed
    total_num_envelopes = num_less_than_five_pounds + num_more_than_five_pounds
    result = total_num_envelopes
    return result

print(solution())