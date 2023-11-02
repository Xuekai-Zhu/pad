def solution():
    """Jessica was trying to win a gift card to her favorite store. To win, she had to guess the total number of red & white jelly beans in the bowl of mixed color jelly beans. She figured it would take three bags of jelly beans to fill up the fishbowl. She assumed that each bag of jellybeans had a similar distribution of colors in each bag. She bought one bag of jellybeans and separated them by color. She had 24 red, 13 black, 36 green, 28 purple, 32 yellow and 18 white. What was Jessica's guess as to how many red and white jelly beans were in the fishbowl?"""
    # Calculate the total number of jelly beans in one bag
    total_jelly_beans = sum([24, 13, 36, 28, 32, 18])

    # Calculate the proportion of red and white jelly beans in one bag
    red_and_white_proportion = (24 + 18) / total_jelly_beans

    # Calculate the number of red and white jelly beans in three bags
    red_and_white_total = int(red_and_white_proportion * total_jelly_beans * 3)

    result = red_and_white_total
    return result

print(solution())