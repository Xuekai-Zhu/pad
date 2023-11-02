def solution():
    """John and Anna bought some eBook readers. John bought 15 eBook readers less than Anna did. Unfortunately, John lost 3 eBook readers. If Anna bought 50 eBook readers, how many eBook readers do they have altogether?"""
    # Define the number of eBook readers Anna bought
    anna_eBook_readers = 50

    # Calculate the number of eBook readers John bought
    john_eBook_readers = anna_eBook_readers - 15

    # Calculate the total number of eBook readers they had before John lost 3
    total_eBook_readers = anna_eBook_readers + john_eBook_readers

    # Calculate the total number of eBook readers they have now after John lost 3
    total_eBook_readers_after_loss = total_eBook_readers - 3
    
    # Display the total number of eBook readers they have now
    result = total_eBook_readers_after_loss
    return result

print(solution())