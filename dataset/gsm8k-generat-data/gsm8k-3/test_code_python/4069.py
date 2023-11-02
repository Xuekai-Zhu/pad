def solution():
    """Sam the butcher made sausage by grinding up 10 pounds of spicy meat mix, loading it into a tube casing, and creating a string of 40 sausage links. Then, she hung up the string of sausage links in her cooler. Later that evening, Brandy, Sam’s Golden Retriever, broke into the cooler and ate 12 links of sausage. After Brandy’s feast, how many ounces of sausage meat were contained in the remaining links?"""
    # Define the weight of the meat mix in pounds
    meat_weight = 10

    # Define the number of sausage links made
    links_made = 40

    # Define the number of links eaten by Brandy
    links_eaten = 12

    # Calculate the weight per link in ounces
    weight_per_link = (16 * meat_weight) / links_made

    # Calculate the weight of the remaining sausage meat in ounces
    remaining_weight = (links_made - links_eaten) * weight_per_link

    # Display the weight of the remaining sausage meat
    result = remaining_weight
    return result

print(solution())