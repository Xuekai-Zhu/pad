def solution():
    """Carly had 42 lollipops to share with her friends. Half of the lollipops were cherry, and the rest were equal amounts of watermelon, sour apple, and grape. How many lollipops were grape?"""
    # Calculate the number of cherry lollipops
    cherry = 42 / 2

    # Calculate the number of non-cherry lollipops
    non_cherry = 42 - cherry

    # Divide the non-cherry lollipops into 3 equal groups
    each_non_cherry = non_cherry / 3

    # Calculate the number of grape lollipops
    grape = each_non_cherry

    # Display the number of grape lollipops
    result = grape
    return result

print(solution())