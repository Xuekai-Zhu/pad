def solution():
    """Alex has 4 pens in the first week of a month. Every week her pen collection doubles. How many more pens will Alex have than Jane if Jane will have 16 pens after a month?"""
    # Calculate Alex's pen collection after a month
    alex_pens = 4 * (2 ** 4)
    
    # Calculate the number of pens Jane will have after a month
    jane_pens = 16
    
    # Calculate the difference between Alex's and Jane's pen collections
    difference = alex_pens - jane_pens
    
    # Display the difference
    result = difference
    return result

print(solution())