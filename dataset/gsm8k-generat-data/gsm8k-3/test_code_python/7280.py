def solution():
    """Vaishali wears a beautiful piece of clothing called a Saree,  a traditional Indian dress for women.  It is mostly tangerine-colored, with blue, brown, and gold-colored decorative stripes.  There are three times as many gold stripes as brown stripes, and five times as many blue stripes as gold stripes. If there are 4 brown stripes, how many blue stripes does Vaishali's Saree have?"""
    # Define the number of brown stripes
    brown_stripes = 4

    # Calculate the number of gold stripes
    gold_stripes = 3 * brown_stripes

    # Calculate the number of blue stripes
    blue_stripes = 5 * gold_stripes

    # Calculate the total number of stripes
    total_stripes = brown_stripes + gold_stripes + blue_stripes

    # Display the number of blue stripes
    result = blue_stripes
    return result

print(solution())