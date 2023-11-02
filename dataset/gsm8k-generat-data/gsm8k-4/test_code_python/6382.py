def solution():
    """A case of water contains 24 bottles. A children's camp comprising of 4 groups purchased 13 cases for a 3-day camp. The first group has 14 children, the second group has 16 children, the third group has 12 children, and the fourth group has half of the number of the first three groups combined. If each child consumes 3 bottles a day, how many more bottles of water does the camp organizer still need to buy?"""
    # Define the number of bottles in a case of water
    BOTTLES_PER_CASE = 24

    # Define the number of days for the camp
    DAYS = 3

    # Calculate the total number of children in the camp
    total_children = 14 + 16 + 12 + (14 + 16 + 12) / 2

    # Calculate the total number of bottles needed for the camp
    total_bottles_needed = total_children * 3 * DAYS

    # Calculate the total number of bottles purchased
    total_bottles_purchased = 13 * BOTTLES_PER_CASE

    # Calculate the number of bottles still needed to be purchased
    bottles_needed = total_bottles_needed - total_bottles_purchased

    result = bottles_needed
    return result

print(solution())