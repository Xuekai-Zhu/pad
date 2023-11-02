def solution():
    """Carl is hosting an open house for his new business. He knows 50 people will show up and hopes that another 40 people will randomly show up. He’s created 10 extravagant gift bags for the first 10 people who visit his shop. He’s made average gift bags for 20 people but needs to make enough for everyone who visits to have one. How many more bags does he need to make?"""
    expected_visitors = 50 + 40
    extravagant_gift_bags = 10
    average_gift_bags = 20
    total_gift_bags = expected_visitors + average_gift_bags
    additional_gift_bags_needed = total_gift_bags - extravagant_gift_bags
    result = additional_gift_bags_needed
    return result

print(solution())