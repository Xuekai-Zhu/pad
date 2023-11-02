def solution():
    """When the strawberries at Fruity Farm are ready for harvest, Miguel charges each interested picker $4 to access the strawberry fields. Once there, people pick as many strawberries as they wish, and then take them to Miguel for weighing and pricing. This year, the standard price of a pound of strawberries is $20. Miguel is a very generous man. He deducts the entrance charge from the cost of the harvest. Sally, Jenny and Moses have just finished their strawberry picking and are headed home. They paid $128 for their harvest. How many pounds of strawberry did they pick?"""
    entrance_fee = 4
    price_per_lb = 20
    total_paid = 128
    harvest_cost = total_paid - entrance_fee*3
    total_pounds = harvest_cost / price_per_lb
    result = total_pounds
    return result

print(solution())