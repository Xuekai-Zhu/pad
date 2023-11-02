def solution():
    five_star = 6
    four_star = 7
    three_star = 4
    two_star = 1
    total_score = five_star * 5 + four_star * 4 + three_star * 3 + two_star * 2
    total_reviews = five_star + four_star + three_star + two_star
    average_score = total_score / total_reviews
    result = average_score
    return result

print(solution())