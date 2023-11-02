def solution():
    """Junior has 16 rabbits. On Monday, he bought 6 toys for his rabbits. On Wednesday, he bought twice as many toys as he did Monday. On Friday, he bought four times as many toys as he did on Monday, and on the next day he bought half as many toys as he did on Wednesday. If he split all the toys evenly between the rabbits, how many toys would each rabbit have?"""
    # Define the number of rabbits and the number of toys bought on Monday
    num_rabbits = 16
    toys_monday = 6

    # Calculate the number of toys bought on Wednesday and Friday
    toys_wednesday = toys_monday * 2
    toys_friday = toys_monday * 4

    # Calculate the number of toys bought on Saturday
    toys_saturday = toys_wednesday / 2

    # Calculate the total number of toys
    total_toys = toys_monday + toys_wednesday + toys_friday + toys_saturday

    # Calculate the number of toys each rabbit would get if toys were split evenly
    toys_per_rabbit = total_toys / num_rabbits

    result = toys_per_rabbit
    return result

print(solution())