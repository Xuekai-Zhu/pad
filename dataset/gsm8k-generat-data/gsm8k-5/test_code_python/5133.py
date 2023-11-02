def solution():
    total_money_raised = 368 + 343 + 279  # The total money raised is the sum of money from tickets, raffle, and sales
    num_classes = 5  # There are 5 classes that the money raised will be shared between

    # Calculate the average amount of money each class will receive
    average_money_per_class = total_money_raised / num_classes
    result = average_money_per_class
    return result

print(solution())