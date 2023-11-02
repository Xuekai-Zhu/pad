def solution():
    """Michelle had some leftover cans of silly string from her birthday party. She split them among Roger and 3 of his friends. Then Roger decided to give 2 of his cans to his brothers so that he now has 4 for himself. How many cans of silly string did Michelle have to start with?"""
    
    # Let's start with Roger, who now has 4 cans after giving 2 to his brothers
    roger_cans = 4 + 2
    
    # Michelle split her cans among Roger and his 3 friends, so they had a total of 4 people
    total_people = 4
    
    # Let's assume that each person received the same number of cans
    cans_per_person = (roger_cans + 3) / total_people
    
    # Michelle had the same number of cans as the sum of all the cans split among them
    michelle_cans = cans_per_person * total_people
    
    result = michelle_cans
    return result

print(solution())