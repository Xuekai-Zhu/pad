def solution():
    """Three friends went out to watch a movie. Mitch paid for their tickets at $7 each. On the other hand, Jam paid for the 2 boxes of popcorn at $1.5 while Jay paid for the 3 cups of milk tea at $3 each. If the three of them will split the total expenses, how much should each contribute?"""
    # Define the cost of each item
    TICKET_COST = 7
    POPCORN_COST = 1.5
    MILK_TEA_COST = 3

    # Define the number of items purchased by each person
    mitch_tickets = 3
    jam_popcorn = 2
    jay_milk_tea = 3

    # Calculate the total cost of the tickets
    total_ticket_cost = mitch_tickets * TICKET_COST

    # Calculate the total cost of the popcorn
    total_popcorn_cost = jam_popcorn * POPCORN_COST

    # Calculate the total cost of the milk tea
    total_milk_tea_cost = jay_milk_tea * MILK_TEA_COST

    # Calculate the total cost of all the items
    total_cost = total_ticket_cost + total_popcorn_cost + total_milk_tea_cost

    # Calculate the amount each person should contribute
    contribution = total_cost / 3

    # Display the amount each person should contribute
    result = contribution
    return result

print(solution())