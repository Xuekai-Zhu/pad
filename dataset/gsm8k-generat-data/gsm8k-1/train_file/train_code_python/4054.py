def solution():
    """Every year, four clowns and thirty children go on a carousel. This year, the candy seller, at the carousel, had 700 candies. The candy seller then sold 20 candies, to each of the clowns and the children, who attended. How many candies did he have left?"""
    num_clowns = 4
    num_children = 30
    total_people = num_clowns + num_children
    candies_per_person = 20
    num_candies_sold = total_people * candies_per_person
    initial_num_candies = 700
    num_candies_left = initial_num_candies - num_candies_sold
    result = num_candies_left
    return result

print(solution())