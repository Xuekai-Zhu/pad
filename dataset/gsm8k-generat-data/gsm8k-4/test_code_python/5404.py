def solution():
    """Lauren sent 65 pieces of mail on Monday, 10 more pieces of mail on Tuesday than on Monday, 5 fewer on Wednesday than on Tuesday, and 15 more pieces of mail on Thursday than on Wednesday. How many pieces of mail did Lauren send?"""
    # Define the number of pieces of mail sent on Monday
    monday = 65

    # Define the number of pieces of mail sent on Tuesday 
    tuesday = monday + 10

    # Define the number of pieces of mail sent on Wednesday
    wednesday = tuesday - 5

    # Define the number of pieces of mail sent on Thursday
    thursday = wednesday + 15

    # Calculate the total number of pieces of mail sent 
    total = monday + tuesday + wednesday + thursday

    # Return the result
    result = total
    return result

print(solution())