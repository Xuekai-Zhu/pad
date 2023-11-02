def solution():
    """Jessica was trying to win a gift card to her favorite store. To win, she had to guess the total number of red & white jelly beans in the bowl of mixed color jelly beans. She figured it would take three bags of jelly beans to fill up the fishbowl. She assumed that each bag of jellybeans had a similar distribution of colors in each bag. She bought one bag of jellybeans and separated them by color. She had 24 red, 13 black, 36 green, 28 purple, 32 yellow and 18 white. What was Jessica's guess as to how many red and white jelly beans were in the fishbowl?"""
    # The ratio of red and white jelly beans in the bag is (24+18)/((24+18)+13+36+28+32) = 42/161
    # Assuming the ratio is similar across all three bags, the number of red and white jelly beans in the fishbowl is 3*(42/161)*(24+18+13+36+28+32) = 78.71
    # Since we have to give a whole number as the guess, we can round up to 79
    jessicas_guess = 79
    result = jessicas_guess
    return result

print(solution())