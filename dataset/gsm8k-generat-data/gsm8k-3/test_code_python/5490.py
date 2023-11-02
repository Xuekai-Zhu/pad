def solution():
    """Junior has 16 rabbits. On Monday, he bought 6 toys for his rabbits. On Wednesday, he bought twice as many toys as he did Monday. On Friday, he bought four times as many toys as he did on Monday, and on the next day he bought half as many toys as he did on Wednesday. If he split all the toys evenly between the rabbits, how many toys would each rabbit have?"""
    # Define the number of rabbits and the number of toys purchased on each day
    num_rabbits = 16
    monday_toys = 6
    wednesday_toys = monday_toys * 2
    friday_toys = monday_toys * 4
    saturday_toys = wednesday_toys / 2

    # Calculate the total number of toys purchased
    total_toys = monday_toys + wednesday_toys + friday_toys + saturday_toys

    # Calculate the number of toys each rabbit would have if they were split evenly
    toys_per_rabbit = total_toys / num_rabbits

    # Display the number of toys per rabbit
    result = toys_per_rabbit
    return result

print(solution())