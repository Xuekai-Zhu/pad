def solution():
    """Aleesia lost 1.5 pounds each week for 10 weeks. Alexei lost 2.5 pounds each week for 8 weeks. How many pounds did the two friends combine to lose?"""
    # Define the weight lost per week for each friend
    ALEESIA_LOSS_PER_WEEK = 1.5
    ALEXEI_LOSS_PER_WEEK = 2.5

    # Define the number of weeks each friend was trying to lose weight
    ALEESIA_WEEKS = 10
    ALEXEI_WEEKS = 8

    # Calculate the total weight lost by Aleesia
    aleesia_total_loss = ALEESIA_LOSS_PER_WEEK * ALEESIA_WEEKS

    # Calculate the total weight lost by Alexei
    alexei_total_loss = ALEXEI_LOSS_PER_WEEK * ALEXEI_WEEKS

    # Calculate the total weight lost by both friends
    total_loss = aleesia_total_loss + alexei_total_loss

    # Display the total weight lost
    result = total_loss
    return result

print(solution())