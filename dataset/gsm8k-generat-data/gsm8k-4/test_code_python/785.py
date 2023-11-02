def solution():
    """On a particular week, Fatima's restaurant served 25 people food and drinks, and 3/5 of that number came to buy coffee. How many people did not buy coffee in the restaurant?"""
    # Define the total number of people served
    total_people = 25

    # Calculate the number of people who came to buy coffee
    coffee_people = total_people * 3/5

    # Calculate the number of people who did not buy coffee
    noncoffee_people = total_people - coffee_people

    # Return the result
    result = noncoffee_people
    return result

print(solution())