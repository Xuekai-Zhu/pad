def solution():
    """Mr. Shaefer harvested 500 lychees in a carton and took them to the market. He sold half of them and took home the remaining number of lychees where they ate 3/5 of them. Calculate the number of lychees remaining."""
    # Define the number of lychees harvested
    lychees = 500

    # Calculate the number of lychees sold at the market
    sold_lychees = lychees / 2

    # Calculate the number of lychees taken home
    remaining_lychees = lychees - sold_lychees

    # Calculate the number of lychees eaten
    eaten_lychees = remaining_lychees * (3/5)

    # Calculate the number of lychees remaining
    remaining_lychees -= eaten_lychees

    # return the result
    result = remaining_lychees
    return result

print(solution())