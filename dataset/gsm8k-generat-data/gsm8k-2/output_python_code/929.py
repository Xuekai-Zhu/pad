def solution():
    """How many apples did two men and three women buy at a certain store if the two men each bought 30 apples, 
    20 less than the number of apples bought by each woman?"""
    men_apples = 30 * 2
    women_apples = (men_apples + 20) * 3
    total_apples = men_apples + women_apples
    result = total_apples
    return result

print(solution())