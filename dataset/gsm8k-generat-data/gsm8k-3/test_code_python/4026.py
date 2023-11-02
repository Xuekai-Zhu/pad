def solution():
    """Mr. Ha owns 5 more silver dollars than Mr. Phung. Mr. Phung has 16 more silver dollars than Mr. Chiu has. If Mr. Chiu has 56 silver dollars, how many silver dollars the three have in total?"""
    # Define the number of silver dollars Mr. Chiu has
    chiu_dollars = 56

    # Calculate the number of silver dollars Mr. Phung has
    phung_dollars = chiu_dollars + 16

    # Calculate the number of silver dollars Mr. Ha has
    ha_dollars = phung_dollars + 5

    # Calculate the total number of silver dollars the three have
    total_dollars = chiu_dollars + phung_dollars + ha_dollars

    # Display the total number of silver dollars
    result = total_dollars
    return result

print(solution())