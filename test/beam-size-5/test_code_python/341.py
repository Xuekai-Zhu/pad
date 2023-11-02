def solution():
    
    # Define the number of tables with 4 legs and 3 legs
    tables_4_legs = 40
    tables_3_legs = 50

    # Calculate the total number of legs in the tables with 4 legs
    total_legs_4_legs = tables_4_legs * 4

    # Calculate the total number of legs in the tables with 3 legs
    total_legs_3_legs = tables_3_legs * 3

    # Calculate the total number of legs in the restaurant's tables
    total_legs = total_legs_4_legs + total_legs_3_legs

    # return the result
    result = total_legs
    return result

print(solution())