def solution():
    """In a studio audience of 100 people, 40% of these people have an envelope taped underneath their chairs. 20% of these people will have "You Won" in their envelope, the rest will have empty envelopes. How many people will win a prize?"""
    # Define the total number of people in the audience
    total_people = 100

    # Calculate the number of people with envelopes taped underneath their chairs
    envelope_people = total_people * 0.4

    # Calculate the number of people who will win a prize
    prize_people = envelope_people * 0.2

    # Return the result
    result = prize_people
    return result

print(solution())