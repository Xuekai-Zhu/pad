def solution():
    """
    Sam the butcher made sausage by grinding up 10 pounds of spicy meat mix, loading it into a tube casing, and creating a string of 40 sausage links.
    Then, she hung up the string of sausage links in her cooler. Later that evening, Brandy, Sam’s Golden Retriever, broke into the cooler and ate 12 links of sausage.
    After Brandy’s feast, how many ounces of sausage meat were contained in the remaining links?
    """
    pounds_of_sausage = 10
    links_of_sausage = 40
    links_eaten_by_brandy = 12
    remaining_links = links_of_sausage - links_eaten_by_brandy
    ounces_of_sausage_per_link = 16
    ounces_of_sausage_total = remaining_links * ounces_of_sausage_per_link
    
    return ounces_of_sausage_total

print(solution())