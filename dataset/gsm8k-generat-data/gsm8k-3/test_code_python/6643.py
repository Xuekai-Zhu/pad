def solution():
    """Yuri has been adopting puppies for a month now. The first week he adopted 20 puppies, the second week 2/5 times as many puppies as the first week, the third week twice the number of puppies he adopted in the second week, and the fourth week ten more puppies than he adopted on the first week. How many puppies does Yuri have now?"""
    # Define the number of puppies adopted in each week
    week1 = 20
    week2 = 2/5 * week1
    week3 = 2 * week2
    week4 = week1 + 10
    
    # Calculate the total number of puppies adopted
    total_puppies = week1 + week2 + week3 + week4
    
    # Display the total number of puppies
    result = total_puppies
    return result

print(solution())