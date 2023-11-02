def solution():
    """Molly and her parents love to hang out at the beach on weekends. Molly spent the better part of the day at the beach and saw 100 people join them. At 5:00, 40 people left the beach. What's the total number of people at the beach if they all stayed until evening?"""
    # Define the initial number of people at the beach
    initial_people = 0

    # Add Molly and her parents to the initial number of people
    initial_people += 3

    # Add the 100 people who joined them during the day
    initial_people += 100

    # Subtract the 40 people who left at 5:00
    final_people = initial_people - 40

    # Display the final number of people at the beach
    result = final_people
    return result

print(solution())