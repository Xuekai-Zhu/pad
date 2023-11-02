def solution():
    """Anna ate 4 apples on Tuesday. On Wednesday, she ate double the apples she ate on Tuesday. On Thursday, Anna ate half the apples she ate on Tuesday. How many apples has Anna eaten by the end of these three days?"""
    # Define the number of apples Anna ate on Tuesday
    tuesday_apples = 4

    # Calculate the number of apples Anna ate on Wednesday
    wednesday_apples = tuesday_apples * 2

    # Calculate the number of apples Anna ate on Thursday
    thursday_apples = tuesday_apples / 2

    # Calculate the total number of apples Anna ate
    total_apples = tuesday_apples + wednesday_apples + thursday_apples

    # return the result
    result = total_apples
    return result

print(solution())