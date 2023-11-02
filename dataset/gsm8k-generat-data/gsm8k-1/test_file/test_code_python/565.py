def solution():
    """Liam and Mitchell own competing lemonade stands across the street from one another. When Liam bragged that he had made $63 one weekend, Mitchell laughed and told Liam he had sold 21 lemonades at $4 apiece the same weekend. How many more dollars did Mitchell make selling lemonade that weekend than Liam?"""
    liam_sales = 63
    mitchell_sales = 21 * 4
    difference = mitchell_sales - liam_sales
    result = difference
    return result

print(solution())