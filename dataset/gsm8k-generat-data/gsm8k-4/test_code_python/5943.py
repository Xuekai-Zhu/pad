def solution():
    """Carly had 42 lollipops to share with her friends. Half of the lollipops were cherry, and the rest were equal amounts of watermelon, sour apple, and grape. How many lollipops were grape?"""
    # Define the total number of lollipops
    total_lollipops = 42

    # Calculate the number of cherry lollipops
    cherry_lollipops = total_lollipops / 2

    # Calculate the number of non-cherry lollipops
    non_cherry_lollipops = total_lollipops - cherry_lollipops

    # Calculate the number of non-cherry lollipops per flavor
    per_flavor_lollipops = non_cherry_lollipops / 3

    # Calculate the number of grape lollipops
    grape_lollipops = per_flavor_lollipops

    # return the result
    result = grape_lollipops
    return result

print(solution())