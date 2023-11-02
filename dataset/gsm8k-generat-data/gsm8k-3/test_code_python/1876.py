def solution():
    """Carl is hosting an open house for his new business.  He knows 50 people will show up and hopes that another 40 people will randomly show up.  He’s created 10 extravagant gift bags for the first 10 people who visit his shop.  He’s made average gift bags for 20 people but needs to make enough for everyone who visits to have one.  How many more bags does he need to make?"""
    # Define the number of expected and potential visitors
    expected_visitors = 50
    potential_visitors = 40

    # Define the number of gift bags made for the first 10 visitors
    extravagant_bags = 10

    # Define the number of average gift bags made
    average_bags = 20

    # Calculate the total number of visitors
    total_visitors = expected_visitors + potential_visitors

    # Calculate the number of additional gift bags needed for all visitors to have one
    additional_bags = total_visitors - extravagant_bags - average_bags

    # Display the number of additional bags needed
    result = additional_bags
    return result

print(solution())