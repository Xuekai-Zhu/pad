def solution():
    """Sam the butcher made sausage by grinding up 10 pounds of spicy meat mix, loading it into a tube casing, and creating a string of 40 sausage links. Then, she hung up the string of sausage links in her cooler. Later that evening, Brandy, Sam’s Golden Retriever, broke into the cooler and ate 12 links of sausage. After Brandy’s feast, how many ounces of sausage meat were contained in the remaining links?"""
    meat_weight = 10 * 16  # convert to ounces
    num_links = 40
    eaten_links = 12
    remaining_links = num_links - eaten_links
    remaining_meat_weight = meat_weight / num_links * remaining_links
    result = remaining_meat_weight
    return result

print(solution())