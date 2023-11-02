def solution():
    """An alien invades Earth. It abducts 200 people. He returns 80% of the people abducted. After that he takes 10 people to another planet. He took the rest to his home planet. How many people did he take to his home planet?"""
    people_abducted = 200
    people_returned = people_abducted * 0.8
    people_left = people_abducted - people_returned
    people_home = people_left - 10
    result = people_home
    return result

print(solution())