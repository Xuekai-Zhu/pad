def solution():
    """John and his two brothers decide to split the cost of an apartment.  It is 40% more expensive than John's old apartment which costs $1200 per month.  How much does John save per year by splitting the apartment compared to living alone?"""
    # Define the cost of John's old apartment
    OLD_APARTMENT_COST = 1200

    # Calculate the cost of the new apartment
    new_apartment_cost = OLD_APARTMENT_COST * 1.4

    # Calculate John's portion of the new apartment cost
    john_cost = new_apartment_cost / 3

    # Calculate John's yearly savings
    yearly_savings = (OLD_APARTMENT_COST - john_cost) * 12

    # Display John's yearly savings
    result = yearly_savings
    return result

print(solution())