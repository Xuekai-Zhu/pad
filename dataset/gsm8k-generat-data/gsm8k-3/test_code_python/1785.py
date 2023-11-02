def solution():
    """Angeli had 90 assorted candies. One-third of the candies were lollipops and the rest were candy canes. She then shared the lollipops equally among the boys such that each boy received 3. She then shared the candy canes equally among the girls such that each received 2. How many boys and girls were given altogether?"""
    # Calculate the number of lollipops
    lollipops = 90 // 3

    # Calculate the number of candy canes
    candy_canes = 90 - lollipops

    # Calculate the number of boys and girls
    boys = lollipops // 3
    girls = candy_canes // 2

    # Calculate the total number of children
    total_children = boys + girls

    # Display the total number of children
    result = total_children
    return result

print(solution())