def solution():
    """Jeff owns a catering company. During a recent event, he sent 8 dozen glasses and 4 dozen plates for the party. When they were returned, 10 glasses were broken as well as 6 plates. How many glasses and plates does Jeff have now?"""
    original_glasses = 8 * 12
    original_plates = 4 * 12
    broken_glasses = 10
    broken_plates = 6
    remaining_glasses = original_glasses - broken_glasses
    remaining_plates = original_plates - broken_plates
    total = remaining_glasses + remaining_plates
    result = total
    return result

print(solution())