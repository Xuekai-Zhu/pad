def solution():
    """When the strawberries at Fruity Farm are ready for harvest, Miguel charges each interested picker $4 to access the strawberry fields. Once there, people pick as many strawberries as they wish, and then take them to Miguel for weighing and pricing. This year, the standard price of a pound of strawberries is $20. Miguel is a very generous man. He deducts the entrance charge from the cost of the harvest. Sally, Jenny and Moses have just finished their strawberry picking and are headed home. They paid $128 for their harvest. How many pounds of strawberry did they pick?"""
    # Define the entrance fee charged by Miguel
    entrance_fee = 4

    # Define the standard price of a pound of strawberries
    price_per_pound = 20

    # Calculate how much money the three pickers paid for the strawberries after Miguel deducted the entrance fee
    harvest_cost = 128 + entrance_fee*3

    # Calculate how many pounds of strawberries they picked
    pounds_picked = harvest_cost / price_per_pound

    # Return the result
    result = pounds_picked
    return result

print(solution())