def solution():
    """A grocery store has 4 kinds of jelly. They sell grape jelly twice as much as strawberry jelly, and raspberry jelly twice as much as plum jelly. The raspberry jelly sells a third as much as the grape jelly. If they sold 6 jars of plum jelly today, how many jars of strawberry jelly did they sell?"""
    
    # Define the number of jars of plum jelly sold
    plum_jelly_sold = 6
    
    # Calculate the number of jars of raspberry jelly sold
    raspberry_jelly_sold = plum_jelly_sold * 2
    
    # Calculate the number of jars of grape jelly sold
    grape_jelly_sold = raspberry_jelly_sold * 3
    
    # Calculate the number of jars of strawberry jelly sold
    strawberry_jelly_sold = grape_jelly_sold / 2
    
    result = strawberry_jelly_sold
    return result

print(solution())