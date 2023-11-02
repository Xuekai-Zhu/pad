def solution():
    """Katy makes coffee using teaspoons of sugar and cups of water in the ratio of 7:13. If she used a total of 120 teaspoons of sugar and cups of water, calculate the number of teaspoonfuls of sugar she used."""
    total_ratio = 7 + 13
    sugar_ratio = 7
    sugar_used = (sugar_ratio/total_ratio) * 120
    result = sugar_used
    return result

print(solution())