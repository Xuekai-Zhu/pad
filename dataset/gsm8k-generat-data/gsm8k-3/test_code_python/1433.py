def solution():
    """Among the career home run leaders for MLB, Hank Aaron has 175 fewer than twice the number that Dave Winfield has.  Hank Aaron hit 755 home runs.  How many home runs did Dave Winfield hit in his career?"""
    # Define the number of home runs hit by Hank Aaron
    hank_aaron_hr = 755

    # Calculate the number of home runs hit by Dave Winfield
    winfield_hr = (hank_aaron_hr / 2) - 175

    # Display the number of home runs hit by Dave Winfield
    result = winfield_hr
    return result

print(solution())