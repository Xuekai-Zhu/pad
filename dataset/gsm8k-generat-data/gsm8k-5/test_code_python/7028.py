def solution():
    total_people = 100  # Total number of people in the studio audience
    envelope_percentage = 0.4  # 40% of people have an envelope taped under their chair
    winning_percentage = 0.2  # 20% of people who have an envelope will have "You Won" in their envelope

    # Calculate the number of people with an envelope
    people_with_envelope = total_people * envelope_percentage

    # Calculate the number of people who will win a prize
    prize_winners = people_with_envelope * winning_percentage
    result = prize_winners
    return result

print(solution())