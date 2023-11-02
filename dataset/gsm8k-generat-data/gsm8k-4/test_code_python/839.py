def solution():
    """The Rotary Club is holding its annual fundraising Omelet Breakfast, with tickets sold in advance. The tickets come in different price levels, for young children, older children, adults, and seniors. This year they sold 53 small children tickets, 35 older children tickets, 75 adult tickets, and 37 senior tickets. To figure out how many eggs they need to buy, the club estimates that small children can eat a half omelet, older children can eat a whole omelet, adults will eat two omelets, and seniors will eat one and a half omelets. Just to be on the safe side, they get enough eggs to make 25 extra omelets. If they use 2 eggs for each omelet, how many eggs will they need to buy?"""
    # Define the number of tickets of each type
    small_children_tickets = 53
    older_children_tickets = 35
    adult_tickets = 75
    senior_tickets = 37

    # Define the number of eggs needed for each type
    small_children_eggs = 0.5
    older_children_eggs = 1
    adult_eggs = 2
    senior_eggs = 1.5

    # Calculate the total number of omelets needed
    total_omelets = (small_children_tickets * small_children_eggs) + \
                    (older_children_tickets * older_children_eggs) + \
                    (adult_tickets * adult_eggs) + \
                    (senior_tickets * senior_eggs)

    # Add 25 extra omelets
    total_omelets += 25

    # Calculate the total number of eggs needed
    total_eggs = total_omelets * 2

    # Return the result
    result = total_eggs
    return result

print(solution())