def solution():
    """Matilda had 20 chocolate bars and shared them evenly amongst herself and her 4 sisters. When her father got home from work, he was upset that they did not put aside any chocolates for him. They felt bad, so they each gave up half of their chocolate bars for their father. Their father then gave 3 chocolate bars to their mother and ate 2. How many chocolate bars did Matilda's father have left?"""
    initial_chocolates = 20
    total_people = 6
    chocolates_per_person = initial_chocolates / total_people
    father_chocolates_received = 0.5 * chocolates_per_person * total_people
    total_chocolates_after_father_received = initial_chocolates - father_chocolates_received
    total_chocolates_after_father_gave_to_mother = total_chocolates_after_father_received - 3
    total_chocolates_after_father_ate = total_chocolates_after_father_gave_to_mother - 2
    result = total_chocolates_after_father_ate
    return result

print(solution())