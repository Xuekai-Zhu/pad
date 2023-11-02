def solution():
    """Bailey bought 8 dog treats and an additional 2 chew toys. She also got 10 more rawhide bones.
       She forgot her money and had to split the charges equally across 4 credit cards. How many items were included in each charge?"""
    # Define the number of items Bailey bought
    treats = 8
    toys = 2
    bones = 10

    # Calculate the total number of items
    total_items = treats + toys + bones

    # Divide the total cost equally among 4 credit cards
    items_per_charge = total_items // 4

    # Display the number of items included in each charge
    result = items_per_charge
    return result

print(solution())