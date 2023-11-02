def solution():
    """Every year, four clowns and thirty children go on a carousel. This year, the candy seller, at the carousel, had 700 candies. The candy seller then sold 20 candies, to each of the clowns and the children, who attended. How many candies did he have left?"""
    clowns = 4
    children = 30
    total_people = clowns + children
    candies = 700
    sold_candies = total_people * 20
    remaining_candies = candies - sold_candies
    result = remaining_candies
    return result

print(solution())