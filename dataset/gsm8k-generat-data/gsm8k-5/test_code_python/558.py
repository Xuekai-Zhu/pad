def solution():
    # Calculate the total value of the gift cards
    total_value = (6 * 500) + (9 * 200)

    # Calculate the value of the gift cards Jack already sent the scammer
    sent_value = (1 * 500) + (2 * 200)

    # Calculate the value of the gift cards Jack can still return
    return_value = total_value - sent_value
    result = return_value
    return result

print(solution())