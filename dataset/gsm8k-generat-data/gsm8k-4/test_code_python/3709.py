def solution():
    """June liked to collect cat stickers. She had a total of 76 in her collection. Her twin sister Bonnie also collected cat stickers and had 63 in her collection. For their birthday, their grandparents gave them 25 cat stickers each. How many combined stickers did they have?"""
    # Define the initial numbers of cat stickers
    june_stickers = 76
    bonnie_stickers = 63

    # Add the number of cat stickers given by their grandparents
    june_stickers += 25
    bonnie_stickers += 25

    # Calculate the total number of cat stickers they have
    total_stickers = june_stickers + bonnie_stickers

    # return the result
    result = total_stickers
    return result

print(solution())