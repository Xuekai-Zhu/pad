def solution():
    total_people = 100
    percent_envelopes = 0.4
    percent_winners = 0.2

    # Calculate the number of people with envelopes taped under their chairs
    num_envelopes = total_people * percent_envelopes

    # Calculate the number of winners
    num_winners = num_envelopes * percent_winners

    result = num_winners
    return result

print(solution())