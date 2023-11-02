def solution():
    """Antoine is having a dinner party and his butcher recommends 1/2 pound of meat per person.  If he's inviting 6 people over and the beef tenderloin is $15 a pound, how much will this cost him?"""
    # Define the recommended amount of meat per person and the price per pound
    meat_per_person = 0.5
    price_per_pound = 15.0

    # Define the number of people attending the dinner party
    num_people = 6

    # Calculate the total amount of meat needed
    total_meat = meat_per_person * num_people

    # Calculate the total cost of the meat
    total_cost = total_meat * price_per_pound

    # Display the total cost
    result = total_cost
    return result

print(solution())