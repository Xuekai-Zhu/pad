def solution():
    
    # Define the number of people Conor saw on the first day
    day1 = 50

    # Define the number of people Conor saw on the second day
    day2 = day1 + 20

    # Define the number of people Conor saw on the third day
    day3 = day2 * 2

    # Calculate the total number of people Conor saw in the first three days
    total_people = day1 + day2 + day3

    # Calculate the total number of people Conor saw in the rest of the week
    total_people += 60 * 7

    # Display the total number of people
    result = total_people
    return result

print(solution())