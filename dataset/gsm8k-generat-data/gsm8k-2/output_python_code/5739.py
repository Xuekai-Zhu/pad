def solution():
    """John and Anna bought some eBook readers. John bought 15 eBook readers less than Anna did. Unfortunately, John lost 3 eBook readers. If Anna bought 50 eBook readers, how many eBook readers do they have altogether?"""
    anna_readers = 50
    john_readers = anna_readers - 15
    total_readers = anna_readers + john_readers - 3
    result = total_readers
    return result

print(solution())