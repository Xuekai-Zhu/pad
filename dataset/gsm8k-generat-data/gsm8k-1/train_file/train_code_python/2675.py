def solution():
    """Jennifer decides to share her sweets between herself and her 3 friends. She has 212 green sweets, 310 blue sweets and 502 yellow sweets. How many sweets will Jennifer and her friends get each?"""
    total_sweets = 212 + 310 + 502
    num_of_people = 4
    sweets_per_person = total_sweets // num_of_people
    result = sweets_per_person
    return result

print(solution())