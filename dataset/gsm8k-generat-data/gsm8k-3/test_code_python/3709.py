def solution():
    """June liked to collect cat stickers.  She had a total of 76 in her collection.  Her twin sister Bonnie also collected cat stickers and had 63 in her collection.  For their birthday, their grandparents gave them 25 cat stickers each.  How many combined stickers did they have?"""
    # Define the number of stickers June and Bonnie had before their birthday
    june_stickers = 76
    bonnie_stickers = 63

    # Define the number of stickers their grandparents gave them
    birthday_stickers = 25

    # Calculate the combined number of stickers after their birthday
    total_stickers = june_stickers + bonnie_stickers + 2 * birthday_stickers

    # Display the total number of stickers
    result = total_stickers
    return result

print(solution())