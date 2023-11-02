def solution():
    """Matilda had 20 chocolate bars and shared them evenly amongst herself and her 4 sisters. When her father got home from work, he was upset that they did not put aside any chocolates for him. They felt bad, so they each gave up half of their chocolate bars for their father. Their father then gave 3 chocolate bars to their mother and ate 2. How many chocolate bars did Matilda's father have left?"""
    # Calculate the number of chocolate bars each person got initially
    initial_bars = 20 / 5

    # Calculate the number of bars given to the father
    father_bars = 2.5 * 4

    # Calculate the number of bars left after the father takes his share
    remaining_bars = 20 - father_bars

    # Calculate the number of bars remaining after the mother takes 3 and the father eats 2
    final_bars = remaining_bars - 3 - 2

    # Display the final number of chocolate bars the father has left
    result = final_bars
    return result

print(solution())