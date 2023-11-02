def solution():
    """Avery puts 4 shirts in the donation box.  He adds twice as many pants as shirts in the box.  He throws in half as many shorts as pants in the box. In total, how many pieces of clothes is Avery donating?"""
    # Define the number of shirts, pants, and shorts added to the box
    shirts = 4
    pants = 2 * shirts
    shorts = int(pants / 2)

    # Calculate the total number of pieces of clothes donated
    total_clothes = shirts + pants + shorts

    # Display the total number of pieces of clothes
    result = total_clothes
    return result

print(solution())