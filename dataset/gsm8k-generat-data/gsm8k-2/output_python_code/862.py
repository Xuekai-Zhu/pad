def solution():
    """In a class of 25 students, students were asked if they like French fries, burgers, or neither. 15 students said they like French fries and 10 said they like burgers, with these statistics including the responses of 6 students who said they like both French fries and burgers. How many students do not like either food?"""
    fries_only = 15 - 6 # students who like only fries
    burgers_only = 10 - 6 # students who like only burgers
    both = 6 # students who like both
    neither = 25 - (fries_only + burgers_only + both) # students who like neither
    result = neither
    return result

print(solution())