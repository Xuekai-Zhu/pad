def solution():
    """Matilda had 20 chocolate bars and shared them evenly amongst herself and her 4 sisters.
    When her father got home from work, he was upset that they did not put aside any chocolates for him.
    They felt bad, so they each gave up half of their chocolate bars for their father.
    Their father then gave 3 chocolate bars to their mother and ate 2.
    How many chocolate bars did Matilda's father have left?"""
    initial_chocolates = 20
    num_people = 6  # Matilda, her 4 sisters, and their father
    chocolates_per_person = initial_chocolates / num_people
    chocolates_for_father = 0.5 * chocolates_per_person * 5
    father_chocolates_left = chocolates_for_father - 3 - 2
    result = father_chocolates_left
    return result

print(solution())