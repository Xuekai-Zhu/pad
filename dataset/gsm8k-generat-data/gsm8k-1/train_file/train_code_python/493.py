def solution():
    """There is a 5,200 sq. ft. house and a 7,300 sq. ft. house next to each other. The smaller house is being expanded. If the new total square footage of both houses is 16,000 sq. ft., how much is the smaller house being expanded by, in sq. ft.?"""
    initial_sqft1 = 5200
    initial_sqft2 = 7300
    total_sqft = 16000
    expanded_sqft1 = total_sqft - initial_sqft2
    expansion = expanded_sqft1 - initial_sqft1
    result = expansion
    return result

print(solution())