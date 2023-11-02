def solution():
    """In a class of 25 students, students were asked if they like French fries, burgers, or neither. 15 students said they like French fries and 10 said they like burgers, with these statistics including the responses of 6 students who said they like both French fries and burgers. How many students do not like either food?"""
    # Define the number of students who like French fries, burgers, or both
    fries = 15
    burgers = 10
    both = 6

    # Calculate the number of students who like neither food
    neither = 25 - (fries + burgers - both)

    # Display the number of students who like neither food
    result = neither
    return result

print(solution())