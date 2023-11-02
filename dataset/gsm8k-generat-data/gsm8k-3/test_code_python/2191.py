def solution():
    """There were 15 males and 10 more girls at the party. Each attendee received 2 cans of soft drinks. If Mary bought several boxes of soft drinks where a box contains 8 cans and is priced at $5 for each box, how much did Mary spend on soft drinks?"""
    # Define the number of males and females at the party
    MALES = 15
    FEMALES = MALES + 10

    # Calculate the total number of attendees
    total_attendees = MALES + FEMALES

    # Calculate the total number of cans of soft drinks needed
    total_cans = total_attendees * 2

    # Calculate the total number of boxes of soft drinks needed
    total_boxes = total_cans // 8 + (total_cans % 8 > 0)

    # Calculate the total cost of the soft drinks
    total_cost = total_boxes * 5

    # Display the total cost
    result = total_cost
    return result

print(solution())