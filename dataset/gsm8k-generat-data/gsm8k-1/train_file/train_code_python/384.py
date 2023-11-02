def solution():
    """When the strawberries at Fruity Farm are ready for harvest, Miguel charges each interested picker $4 to access the strawberry fields. Once there, people pick as many strawberries as they wish, and then take them to Miguel for weighing and pricing. This year, the standard price of a pound of strawberries is $20. Miguel is a very generous man. He deducts the entrance charge from the cost of the harvest. Sally, Jenny and Moses have just finished their strawberry picking and are headed home. They paid $128 for their harvest. How many pounds of strawberry did they pick?"""
    entrance_fee = 4
    price_per_pound = 20
    total_cost = 128
    total_pounds = (total_cost - entrance_fee) / price_per_pound
    result = total_pounds
    return result

print(solution())