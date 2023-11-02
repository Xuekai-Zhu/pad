def solution():
    """Michelle had some leftover cans of silly string from her birthday party. She split them among Roger and 3 of his friends. Then Roger decided to give 2 of his cans to his brothers so that he now has 4 for himself. How many cans of silly string did Michelle have to start with?"""
    friends = 3
    roger_cans = 4
    brother_cans = 2
    total_cans = roger_cans + brother_cans
    michelle_cans = (total_cans + friends) * 4
    result = michelle_cans
    return result

print(solution())