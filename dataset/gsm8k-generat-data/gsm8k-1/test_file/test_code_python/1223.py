def solution():
    """Susan orders 3 magazines that send 12 issues a year. She has 1 magazine that sends 6 issues a year. Her last magazine sends her 4 times the amount of the 6 issue magazine. How many magazines does she get every year?"""
    magazines_ordered = 3
    issues_per_magazine = 12
    total_issues = magazines_ordered * issues_per_magazine
    other_magazine = 6
    third_magazine = other_magazine * 4
    total_magazines = magazines_ordered + 2
    total_magazines += (total_issues / other_magazine)
    total_magazines += (total_issues / third_magazine)
    result = total_magazines
    return result

print(solution())