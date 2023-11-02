def solution():
    """John and Anna bought some eBook readers. John bought 15 eBook readers less than Anna did.
    Unfortunately, John lost 3 eBook readers. If Anna bought 50 eBook readers, how many eBook readers do they have altogether?"""
    
    # Define the number of eBook readers Anna bought
    anna_ebooks = 50

    # Define the number of eBook readers John bought
    john_ebooks = anna_ebooks - 15

    # Subtract 3 from the number of eBook readers John has
    john_ebooks -= 3

    # Calculate the total number of eBook readers they have
    total_ebooks = anna_ebooks + john_ebooks

    # return the result
    result = total_ebooks
    return result

print(solution())