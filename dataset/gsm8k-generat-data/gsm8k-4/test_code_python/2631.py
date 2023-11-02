def solution():
    """Jenson and Kingsley have a tailoring business. Jenson makes 3 shirts, and Kingsley makes 5 pairs of pants per day. If each shirt uses 2 yards of fabric and a pair of pants uses 5 yards of fabric, how many yards of fabric do they need every 3 days?"""
    # Define the number of days to consider
    days = 3

    # Define the number of shirts and pants made per day
    shirts_per_day = 3
    pants_per_day = 5

    # Define the fabric used for each shirt and pair of pants
    fabric_per_shirt = 2
    fabric_per_pants = 5

    # Calculate the total fabric used for shirts and pants for 3 days
    total_shirt_fabric = shirts_per_day * fabric_per_shirt * days
    total_pants_fabric = pants_per_day * fabric_per_pants * days

    # Calculate the total fabric needed for 3 days
    total_fabric = total_shirt_fabric + total_pants_fabric

    # return the result
    result = total_fabric
    return result

print(solution())