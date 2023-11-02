def solution():
    """Jessica was trying to win a gift card to her favorite store.  To win, she had to guess the total number of red & white jelly beans in the bowl of mixed color jelly beans. She figured it would take three bags of jelly beans to fill up the fishbowl.  She assumed that each bag of jellybeans had a similar distribution of colors in each bag.  She bought one bag of jellybeans and separated them by color.  She had 24 red, 13 black, 36 green, 28 purple, 32 yellow and 18 white.  What was Jessica's guess as to how many red and white jelly beans were in the fishbowl?"""
    # Find the total number of jelly beans in one bag
    total_count = sum([24, 13, 36, 28, 32, 18])

    # Calculate the fraction of jelly beans in one bag that are red or white
    red_white_frac = (24+18)/total_count

    # Estimate the number of red and white jelly beans in the fishbowl
    estimated_count = round(red_white_frac * total_count * 3)

    # Display the estimated count of red and white jelly beans
    result = estimated_count
    return result

print(solution())