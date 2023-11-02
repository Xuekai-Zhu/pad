def solution():
    """John and Anna bought some eBook readers. John bought 15 eBook readers less than Anna did. Unfortunately, John lost 3 eBook readers. If Anna bought 50 eBook readers, how many eBook readers do they have altogether?"""
    anna = 50
    john = anna - 15
    john -= 3    # lost 3 eBook readers
    total = anna + john
    result = total
    return result

print(solution())