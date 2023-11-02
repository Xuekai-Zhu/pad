def solution():
    """Jessica was trying to win a gift card to her favorite store. To win, she had to guess the total number of red & white jelly beans in the bowl of mixed color jelly beans. She figured it would take three bags of jelly beans to fill up the fishbowl. She assumed that each bag of jellybeans had a similar distribution of colors in each bag. She bought one bag of jellybeans and separated them by color. She had 24 red, 13 black, 36 green, 28 purple, 32 yellow and 18 white. What was Jessica's guess as to how many red and white jelly beans were in the fishbowl?"""
    total_jellybeans = 3 * (24 + 13 + 36 + 28 + 32 + 18) #total jellybeans in the fishbowl
    red_white_ratio = (24 + 18) / (24 + 13 + 36 + 28 + 32 + 18) #ratio of red and white jellybeans in one bag of jellybeans
    red_white_jellybeans = round(total_jellybeans * red_white_ratio) #estimated number of red and white jellybeans in the fishbowl
    result = red_white_jellybeans
    return result

print(solution())