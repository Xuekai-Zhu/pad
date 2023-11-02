def solution():
    """Bryce is bringing in doughnuts for his class. There are 25 students in his class, 10 kids want chocolate doughnuts and 15 want glazed doughnuts. The chocolate doughnuts cost $2 each and the glazed doughnuts cost $1 each. How much is the total cost for doughnuts?"""
    # Define the number of students, number of chocolate doughnut lovers, price of chocolate doughnuts, and number of glazed doughnut lovers, price of glazed doughnuts
    students = 25
    choc_doughnut_lovers = 10
    choc_doughnut_price = 2
    glazed_doughnut_lovers = 15
    glazed_doughnut_price = 1

    # Calculate the total cost of chocolate doughnuts and glazed doughnuts
    choc_doughnut_cost = choc_doughnut_lovers * choc_doughnut_price
    glazed_doughnut_cost = glazed_doughnut_lovers * glazed_doughnut_price

    # Calculate the total cost of all the doughnuts
    total_cost = choc_doughnut_cost + glazed_doughnut_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())