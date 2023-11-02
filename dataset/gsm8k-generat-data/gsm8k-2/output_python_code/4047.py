def solution():
    """Ivanka wrote a book that took her 3 more months than it took Woody to write a book. Woody spent 1.5 years writing his book. How many months in total did Ivanka and Woody need to write their books?"""
    woody_time_in_months = 1.5 * 12
    ivanka_time_in_months = woody_time_in_months + 3
    total_time_in_months = woody_time_in_months + ivanka_time_in_months
    result = total_time_in_months
    return result

print(solution())