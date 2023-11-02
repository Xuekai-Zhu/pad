def solution():
    """Avery puts 4 shirts in the donation box. He adds twice as many pants as shirts in the box. He throws in half as many shorts as pants in the box. In total, how many pieces of clothes is Avery donating?"""
    # Define the number of shirts
    shirts = 4

    # Calculate the number of pants (twice the number of shirts)
    pants = shirts * 2

    # Calculate the number of shorts (half the number of pants)
    shorts = pants/2

    # Calculate the total number of clothes donated
    total_clothes = shirts + pants + shorts

    # return the result
    result = total_clothes
    return result

print(solution())