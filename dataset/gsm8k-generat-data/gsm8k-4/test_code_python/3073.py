def solution():
    """Bailey bought 8 dog treats and an additional 2 chew toys. She also got 10 more rawhide bones. Sadly, she forgot her money and had to split the charges equally across 4 credit cards. How many items were included in each charge?"""
    # Define the number of treats, chew toys, and bones
    treats = 8
    chew_toys = 2
    bones = 10

    # Calculate the total number of items
    total_items = treats + chew_toys + bones

    # Divide the total number of items by the number of credit cards to get the number of items per charge
    items_per_charge = total_items / 4

    # return the result
    result = items_per_charge
    return result

print(solution())