def solution():
    """The Super Soup franchise had 23 stores in 2018. In 2019, the business opened 5 new stores, but closed the 2 that performed the worst.
    And in 2020, they opened 10 new stores, closing the 6 worst-performing. How many stores did Super Soup have at the end of 2020?"""
    # Define the number of stores in 2018
    stores_2018 = 23

    # Calculate the number of stores in 2019
    stores_2019 = stores_2018 + 5 - 2

    # Calculate the number of stores in 2020
    stores_2020 = stores_2019 + 10 - 6

    # Display the total number of stores in 2020
    result = stores_2020
    return result

print(solution())