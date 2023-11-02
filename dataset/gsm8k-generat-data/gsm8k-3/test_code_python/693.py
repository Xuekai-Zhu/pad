def solution():
    """Ian had twenty roses. He gave six roses to his mother, nine roses to his grandmother, four roses to his sister, and he kept the rest. How many roses did Ian keep?"""
    # Define the number of roses Ian started with
    total_roses = 20

    # Define the number of roses Ian gave to his mother, grandmother, and sister
    mother_roses = 6
    grandmother_roses = 9
    sister_roses = 4

    # Calculate the number of roses Ian kept
    kept_roses = total_roses - mother_roses - grandmother_roses - sister_roses

    # Display the number of roses Ian kept
    result = kept_roses
    return result

print(solution())