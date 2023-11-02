def solution():
    """Stephanie is moving into a new apartment. She needs to figure out how many pieces of silverware she should purchase. She needs spoons, butter knives, steak knives, and forks. For herself she figures 5 of each would be sufficient. But in case she has guests, she wants to have 10 extra pieces of each type. Then she realizes that if everything is clean at the same time, that she will have too many of everything and not enough room to fit them in her kitchen silverware drawer. So she decides to purchase 4 fewer spoons, 4 fewer butter knives, 5 fewer steak knives, and 3 fewer forks. How many pieces total of all the silverware is Stephanie going to buy?"""
    # Define the initial number of silverware pieces for one person
    num_pieces_per_person = 5

    # Define the extra number of silverware needed for guests
    num_extra_guests = 10

    # Calculate the total number of silverware pieces needed for one person with guests
    num_pieces_per_person_guests = num_pieces_per_person + num_extra_guests

    # Adjust the number of spoons, butter knives, steak knives, and forks based on Stephanie's new decision
    num_spoons = num_pieces_per_person_guests - 4
    num_butter_knives = num_pieces_per_person_guests - 4
    num_steak_knives = num_pieces_per_person_guests - 5
    num_forks = num_pieces_per_person_guests - 3

    # Calculate the total number of silverware pieces needed
    total_num_pieces = num_spoons + num_butter_knives + num_steak_knives + num_forks

    # Return the result
    result = total_num_pieces
    return result

print(solution())