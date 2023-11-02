def solution():
    """If a classroom has 3 times as many girls as they do boys, and 1/10 as many nongendered children as they do boys, and the classroom has 30 boys. How many total children does it have?"""
    boys = 30
    girls = boys * 3
    nongendered = boys // 10
    total_children = boys + girls + nongendered
    result = total_children
    return result

print(solution())