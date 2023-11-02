def solution():
    """Candace decides to enter a race. The race is run in 4 segments, with racers eliminated at the end of each segment. 10 racers are eliminated after the first segment. A third of the remaining racers are eliminated after the next section. Half of the remaining racers are eliminated before the last leg of the race. If 100 racers started the race, how many will run in the final section of the race?"""
    # Define the initial number of racers
    initial_racers = 100

    # Calculate the number of racers eliminated after the first segment
    eliminated_segment_1 = 10

    # Calculate the number of racers remaining after the first segment
    remaining_racers_1 = initial_racers - eliminated_segment_1

    # Calculate the number of racers eliminated after the second segment
    eliminated_segment_2 = remaining_racers_1 / 3

    # Calculate the number of racers remaining after the second segment
    remaining_racers_2 = remaining_racers_1 - eliminated_segment_2

    # Calculate the number of racers eliminated before the final section
    eliminated_section_4 = remaining_racers_2 / 2

    # Calculate the number of racers running in the final section
    remaining_racers_final = remaining_racers_2 - eliminated_section_4

    # Return the result
    result = remaining_racers_final
    return result

print(solution())