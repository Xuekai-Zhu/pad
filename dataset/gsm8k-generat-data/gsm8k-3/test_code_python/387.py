def solution():
    """When the strawberries at Fruity Farm are ready for harvest, Miguel charges each interested picker $4 to access the strawberry fields. Once there, people pick as many strawberries as they wish, and then take them to Miguel for weighing and pricing. This year, the standard price of a pound of strawberries is $20. Miguel is a very generous man. He deducts the entrance charge from the cost of the harvest. Sally, Jenny and Moses have just finished their strawberry picking and are headed home. They paid $128 for their harvest. How many pounds of strawberry did they pick?"""
    # Define the entrance fee and the price per pound of strawberries
    ENTRANCE_FEE = 4
    PRICE_PER_POUND = 20

    # Define the total amount paid by Sally, Jenny, and Moses
    total_paid = 128

    # Calculate the amount paid for the strawberries alone
    amount_paid_for_strawberries = total_paid - (3 * ENTRANCE_FEE)

    # Calculate the total weight of the strawberries picked
    total_weight = amount_paid_for_strawberries / PRICE_PER_POUND

    # Display the total weight of strawberries picked
    result = total_weight
    return result

print(solution())