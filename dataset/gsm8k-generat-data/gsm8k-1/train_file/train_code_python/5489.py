def solution():
    """Junior has 16 rabbits. On Monday, he bought 6 toys for his rabbits. On Wednesday, he bought twice as many toys as he did Monday. On Friday, he bought four times as many toys as he did on Monday, and on the next day he bought half as many toys as he did on Wednesday. If he split all the toys evenly between the rabbits, how many toys would each rabbit have?"""
    rabbits = 16
    monday_toys = 6
    wednesday_toys = monday_toys * 2
    friday_toys = monday_toys * 4
    saturday_toys = wednesday_toys / 2
    total_toys = monday_toys + wednesday_toys + friday_toys + saturday_toys
    toys_per_rabbit = total_toys / rabbits
    result = toys_per_rabbit
    return result

print(solution())