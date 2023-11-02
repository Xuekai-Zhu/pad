def solution():
    """Amanda and her family are going to re-paint all the walls inside their house. Before they get started they want to divide up the work. Since all the rooms in the house have different numbers and sizes of walls in them, they figure the fairest way to divide up the work is to count all the walls in the house and assign an equal number to each person. There are 5 people in Amanda's family, including herself. There are 9 rooms in the house. 5 of the rooms have 4 walls each. The other 4 rooms each have 5 walls each. To be fair, how many walls should each person in Amanda's family paint?"""
    num_people = 5
    num_rooms = 9
    num_four_walls_rooms = 5
    num_five_walls_rooms = 4
    num_walls = (num_four_walls_rooms * 4) + (num_five_walls_rooms * 5)
    walls_per_person = num_walls // num_people
    result = walls_per_person
    return result

print(solution())