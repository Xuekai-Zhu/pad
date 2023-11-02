def solution():
    """Matilda had 20 chocolate bars and shared them evenly amongst herself and her 4 sisters. When her father got home from work, he was upset that they did not put aside any chocolates for him. They felt bad, so they each gave up half of their chocolate bars for their father. Their father then gave 3 chocolate bars to their mother and ate 2. How many chocolate bars did Matilda's father have left?"""
    # Define the initial number of chocolate bars
    initial_bars = 20

    # Calculate the number of people who shared the chocolate bars
    num_people = 5

    # Calculate the number of chocolate bars each person received, and the number left for the father
    bars_each = initial_bars // num_people
    bars_father = initial_bars - (bars_each * num_people)

    # Calculate the number of bars each person gives up for the father
    given_bars_each = bars_each / 2

    # Calculate the number of bars left for the father after everyone gives up half
    bars_father += (given_bars_each * num_people)
    
    # Calculate the number of bars left after the father gives 3 to the mother and eats 2
    bars_father -= 3 + 2

    # Return the number of chocolate bars the father has left
    result = bars_father
    return result

print(solution())