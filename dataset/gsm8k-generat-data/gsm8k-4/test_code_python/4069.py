def solution():
    """Sam the butcher made sausage by grinding up 10 pounds of spicy meat mix, loading it into a tube casing, and creating a string of 40 sausage links. Then, she hung up the string of sausage links in her cooler. Later that evening, Brandy, Sam’s Golden Retriever, broke into the cooler and ate 12 links of sausage. After Brandy’s feast, how many ounces of sausage meat were contained in the remaining links?"""
    # Define the initial weight and number of links
    initial_weight = 10 # in pounds
    initial_links = 40

    # Define the number of links eaten by Brandy
    eaten_links = 12

    # Calculate the remaining links and weight
    remaining_links = initial_links - eaten_links
    remaining_weight = initial_weight * (remaining_links / initial_links)

    # Convert the remaining weight to ounces
    remaining_weight_ounces = remaining_weight * 16

    # Calculate the weight of sausage meat in each remaining link
    meat_per_link = remaining_weight_ounces / remaining_links

    result = meat_per_link
    return result

print(solution())