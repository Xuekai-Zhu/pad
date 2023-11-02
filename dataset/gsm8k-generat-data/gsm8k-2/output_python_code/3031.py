def solution():
    """Tedra is harvesting his tomatoes. He harvests 400 kg on Wednesday, and half as much on Thursday. He harvests a total of 2000 kg on Wednesday, Thursday, and Friday. How many tomatoes of the number he harvested on Friday are remaining if he gives away 700kg of them to his friends?"""
    wednesday_harvest = 400
    thursday_harvest = wednesday_harvest / 2
    friday_harvest = 2000 - wednesday_harvest - thursday_harvest
    remaining_harvest = friday_harvest - 700
    result = remaining_harvest
    return result

print(solution())