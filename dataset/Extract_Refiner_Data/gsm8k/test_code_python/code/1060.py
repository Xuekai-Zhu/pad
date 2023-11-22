def solution():
    
    # Define the number of classes visited on each day
    monday_visitors = 32
    tuesday_visitors = monday_visitors * 2
    wednesday_visitors = tuesday_visitors * 3
    thursday_visitors = thursday_visitors + 25
    friday_visitors = friday_visitors + 30

    # Calculate the total number of classes visited
    total_visitors = monday_visitors + tuesday_visitors + wednesday_visitors + thursday_visitors + friday_visitors

    # Display the total number of classes visited
    result = total_visitors
    return result

print(solution())