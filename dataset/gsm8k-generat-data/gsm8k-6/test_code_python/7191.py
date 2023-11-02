def solution():
    # Calculate the number of seashells picked on Tuesday
    seashells_Tuesday = 30/2  

    # Calculate the total number of seashells picked
    total_seashells = 30 + seashells_Tuesday  

    # Calculate the total amount of money Sally can make by selling all the seashells
    total_money = total_seashells * 1.20  
    result = total_money
    return result

print(solution())