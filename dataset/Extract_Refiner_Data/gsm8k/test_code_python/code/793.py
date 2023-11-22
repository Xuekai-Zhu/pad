def solution():
    
    # Define the length of each item
    DECK_LENGTH = 150
    JONES_LENGTH = 240

    # Define the number of items purchased
    desck_count = 2
    jingle_count = 1

    # Calculate the total length of the purchase
    total_length = (DECK_LENGTH * desck_count) + (JONES_LENGTH * jingle_count)

    # Display the total length of the purchase
    result = total_length
    return result

print(solution())