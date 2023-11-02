def solution():
    """One of the clubs at Georgia's school was selling carnations for a fundraising event. A carnation costs $0.50.  They also had a special where you could buy one dozen carnations for $4.00.  If Georgia sent a dozen carnations to each of her 5 teachers and bought one carnation for each of her 14 friends, how much money would she spend?"""
    # Define the cost of a single carnation and a dozen carnations
    SINGLE_PRICE = 0.5
    DOZEN_PRICE = 4.0
    CARNATIONS_PER_DOZEN = 12

    # Calculate the number of carnations Georgia needs to buy
    carnations_for_teachers = 5 * CARNATIONS_PER_DOZEN
    carnations_for_friends = 14
    total_carnations = carnations_for_teachers + carnations_for_friends

    # Calculate the number of dozens and single carnations needed
    dozens_needed = total_carnations // CARNATIONS_PER_DOZEN
    single_carnations_needed = total_carnations % CARNATIONS_PER_DOZEN

    # Calculate the total cost of the carnations
    total_cost = dozens_needed * DOZEN_PRICE + single_carnations_needed * SINGLE_PRICE

    # Display the total cost
    result = total_cost
    return result

print(solution())