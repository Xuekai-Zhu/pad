def solution():
    """In a class of 25 students, students were asked if they like French fries, burgers, or neither. 
    15 students said they like French fries and 10 said they like burgers, with these statistics including the 
    responses of 6 students who said they like both French fries and burgers. How many students do not like either food?"""
    total_students = 25
    fries = 15
    burgers = 10
    both = 6
    neither = total_students - (fries + burgers - both)
    result = neither
    return result

print(solution())