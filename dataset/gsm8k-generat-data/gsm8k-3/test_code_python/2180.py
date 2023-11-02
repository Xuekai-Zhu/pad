def solution():
    """A group of six friends planned to buy a car. The cost of the car is $1700 and they plan to share the cost equally. They had a car wash to help raise funds, which would be taken out of the total cost. The remaining cost would be split between the six friends. At the car wash, they earn $500. However, Brad decided not to join in the purchase of the car. How much more does each friend have to pay now that Brad isn't participating?"""
    # Define the cost of the car and the number of people sharing the cost
    CAR_COST = 1700
    NUM_PEOPLE = 6

    # Calculate the total amount raised from the car wash
    carwash_amount = 500

    # Calculate the remaining cost of the car after taking out the carwash amount
    remaining_cost = CAR_COST - carwash_amount

    # Calculate the cost per person if all six friends paid equally
    cost_per_person = remaining_cost / NUM_PEOPLE

    # Calculate the cost per person without Brad's participation
    cost_per_person_without_brad = remaining_cost / (NUM_PEOPLE - 1)

    # Calculate the difference in cost per person with and without Brad's participation
    cost_difference = cost_per_person_without_brad - cost_per_person

    # Display the additional cost per person without Brad's participation
    result = cost_difference
    return result

print(solution())