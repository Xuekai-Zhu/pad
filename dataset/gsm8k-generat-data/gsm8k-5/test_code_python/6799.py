def solution():
    initial_samsung = 14
    final_samsung = 10
    initial_iphone = 8
    final_iphone = 5
    damaged_samsung = 2
    defective_iphone = 1

    # Calculate the total number of Samsungs sold
    sold_samsung = initial_samsung - final_samsung + damaged_samsung

    # Calculate the total number of iPhones sold
    sold_iphone = initial_iphone - final_iphone + defective_iphone

    # Calculate the total number of cell phones sold
    total_sold = sold_samsung + sold_iphone
    result = total_sold
    return result

print(solution())