def solution():
    """Rose went to the store on Monday and bought 4 cakes. Tuesday she went to a different store and bought three times that number of cakes. On Wednesday she went to another store and bought 5 times the number of cakes she did on Tuesday. How many cakes did she buy after all three days?"""
    monday_cakes = 4
    tuesday_cakes = monday_cakes * 3
    wednesday_cakes = tuesday_cakes * 5
    total_cakes = monday_cakes + tuesday_cakes + wednesday_cakes
    result = total_cakes
    return result

print(solution())