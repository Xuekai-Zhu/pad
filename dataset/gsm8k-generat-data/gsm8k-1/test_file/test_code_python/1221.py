def solution():
    """Carly is making cupcakes and brownies for her art class. She makes 2 less than three times as many brownies as cupcakes. If Carly's class has five people and each person gets two treats, how many cupcakes did Carly make?"""
    num_people = 5
    treats_per_person = 2
    total_treats = num_people * treats_per_person
    brownies_per_cupcake = 3
    cupcakes = (total_treats - 2) / (brownies_per_cupcake + 1)
    result = cupcakes
    return result

print(solution())