def solution():
    """Grandma left $124,600 in her will. She gave half of it to her favorite grandchild, Shelby. The rest was to be evenly divided among the remaining 10 grandchildren. How many dollars did one of the remaining 10 grandchildren receive?"""
    # Define the total amount left after Shelby's portion
    remaining_amount = 124600 / 2

    # Calculate the amount each grandchild receives
    per_grandchild_amount = remaining_amount / 10

    # Return the result
    result = per_grandchild_amount
    return result

print(solution())