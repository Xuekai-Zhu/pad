def solution():
    """Carl is hosting an open house for his new business. He knows 50 people will show up and hopes that another 40 people will randomly show up. He’s created 10 extravagant gift bags for the first 10 people who visit his shop. He’s made average gift bags for 20 people but needs to make enough for everyone who visits to have one. How many more bags does he need to make?"""
    # Define the number of expected guests and gift bags
    expected_guests = 50
    additional_guests = 40
    extravagant_gift_bags = 10
    average_gift_bags = 20

    # Calculate the total number of gift bags needed
    total_gift_bags = expected_guests + additional_guests

    # Calculate the number of gift bags still needed
    remaining_gift_bags = total_gift_bags - extravagant_gift_bags - average_gift_bags

    # return the result
    result = remaining_gift_bags
    return result

print(solution())