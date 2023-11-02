def solution():
    """Ivanka wrote a book that took her 3 more months than it took Woody to write a book. Woody spent 1.5 years writing his book. How many months in total did Ivanka and Woody need to write their books?"""
    woody_time = 1.5 * 12 #convert 1.5 years to months
    ivanka_time = woody_time + 3
    total_time = woody_time + ivanka_time
    result = total_time
    return result

print(solution())