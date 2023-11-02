def solution():
    """Harvey's started out with 25 steaks. Then he sold some, and only had 12 steaks left. He sold 4 more steaks, at 10 dollars. How many steaks did he sell in all?"""
    starting_steaks = 25
    remaining_steaks = 12
    sold_steaks = starting_steaks - remaining_steaks
    additional_sold_steaks = 4
    total_sold_steaks = sold_steaks + additional_sold_steaks
    result = total_sold_steaks
    return result

print(solution())