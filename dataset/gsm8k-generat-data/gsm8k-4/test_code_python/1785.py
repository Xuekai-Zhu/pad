def solution():
    """Angeli had 90 assorted candies. One-third of the candies were lollipops and the rest were candy canes. 
    She then shared the lollipops equally among the boys such that each boy received 3. 
    She then shared the candy canes equally among the girls such that each received 2. How many boys and girls were given altogether?"""
    
    # Define the total number of candies and the number of lollipops
    total_candies = 90
    lollipops = total_candies // 3

    # Calculate the number of candy canes and the number of girls
    candy_canes = total_candies - lollipops
    girls = candy_canes // 2

    # Calculate the number of boys
    boys = lollipops // 3
    
    # Calculate the total number of children
    total_children = girls + boys
    
    # return the result
    result = total_children
    return result

print(solution())