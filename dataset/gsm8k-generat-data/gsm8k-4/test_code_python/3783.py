def solution():
    """Bryce is bringing in doughnuts for his class. There are 25 students in his class, 10 kids want chocolate doughnuts and 15 want glazed doughnuts. The chocolate doughnuts cost $2 each and the glazed doughnuts cost $1 each. How much is the total cost for doughnuts?"""
    # Define the number of students and the number of each type of doughnut
    total_students = 25
    chocolate_doughnuts = 10
    glazed_doughnuts = 15

    # Calculate the cost of the chocolate doughnuts and the glazed doughnuts
    chocolate_cost = chocolate_doughnuts * 2
    glazed_cost = glazed_doughnuts * 1

    # Calculate the total cost of the doughnuts
    total_cost = chocolate_cost + glazed_cost

    # Return the result
    result = total_cost
    return result

print(solution())