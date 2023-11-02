def solution():
    # Calculate the number of children the farmer has
    for i in range(1, 10):
        total_apples = i * 15  # each bag was filled with 15 apples each
        total_apples -= 2*4  # 2 of the children have eaten 4 apples each
        total_apples -= 7  # another child sold 7 of his apples
        if total_apples == 60:  # they had a total of 60 apples left
            result = i
            return result

print(solution())