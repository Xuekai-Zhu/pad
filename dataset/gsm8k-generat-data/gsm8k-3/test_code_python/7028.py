def solution():
    """In a studio audience of 100 people, 40% of these people have an envelope taped underneath their chairs.  20% of these people will have "You Won" in their envelope, the rest will have empty envelopes. How many people will win a prize?"""
    # Define the number of people in the studio audience
    audience_size = 100

    # Calculate the number of people with envelopes taped underneath their chairs
    envelopes = audience_size * 0.4

    # Calculate the number of people who will win a prize
    winners = envelopes * 0.2

    # Display the number of winners
    result = winners
    return result

print(solution())