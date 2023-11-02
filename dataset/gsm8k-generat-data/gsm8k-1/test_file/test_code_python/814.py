def solution():
    """Joe has twice as many cars as Robert. He sells 20% of them and gives away twice as many cars as the number he sold to his mother.
    If Robert has 20 cars, how many cars does Joe remain with after selling and giving some to his mother?"""
    robert_cars = 20
    joe_cars = robert_cars * 2
    percent_sold = 20
    cars_sold = joe_cars * (percent_sold / 100)
    cars_given = cars_sold * 2
    cars_remaining = joe_cars - (cars_sold + cars_given)
    result = cars_remaining
    
    return result

print(solution())