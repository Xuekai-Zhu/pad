def solution():
    """An apple orchard sells apples in bags of 10. The orchard sold a total of 2000 apples one day. How much did an orchard earn for selling this at $5 per bag?"""
    total_apples = 2000
    apples_per_bag = 10
    bags_sold = total_apples / apples_per_bag
    bag_price = 5
    total_earnings = bags_sold * bag_price
    result = total_earnings
    return result

print(solution())