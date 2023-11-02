def solution():
    # Calculate the number of batches needed to fulfill the customer's order
    batches_needed = 60/10  # each batch can make 10 bags of jerky
    batches_needed -= 2  # account for the 20 bags of jerky already made

    # Calculate the number of days it will take to fulfill the order
    days_needed = int(batches_needed) + 1  # it takes one night to make each batch
    result = days_needed
    return result

print(solution())