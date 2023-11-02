def solution():
    # Number of hotdogs Ella and Emma want
    hotdogs_ella = 2
    hotdogs_emma = 2

    # Luke eats twice the amount of hotdogs as his sisters
    hotdogs_luke = hotdogs_ella * 2 + hotdogs_emma * 2

    # Hunter eats 1.5 times the total amount of his sisters
    hotdogs_hunter = (hotdogs_ella + hotdogs_emma) * 1.5

    # Total number of hotdogs needed
    total_hotdogs = hotdogs_ella + hotdogs_emma + hotdogs_luke + hotdogs_hunter
    result = total_hotdogs
    return result

print(solution())