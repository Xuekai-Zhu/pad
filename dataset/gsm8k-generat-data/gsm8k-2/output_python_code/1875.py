def solution():
    """Carl is hosting an open house for his new business. He knows 50 people will show up and hopes that another 40 people will randomly show up. He’s created 10 extravagant gift bags for the first 10 people who visit his shop. He’s made average gift bags for 20 people but needs to make enough for everyone who visits to have one. How many more bags does he need to make?"""
    total_people = 50 + 40
    gift_bags = 10 + 20
    extra_bags_needed = total_people - gift_bags
    result = extra_bags_needed
    return result

print(solution())