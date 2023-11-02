def solution():
    """A trolley driver picked up 10 people on his 1st stop. On the next stop, 3 people got off and twice as many people from the 1st stop got on. On the third stop, 18 people got off and 2 got on. How many people are currently on the trolley?"""
    # Initialize the number of people on the trolley
    num_people = 10

    # Second stop
    num_people -= 3  # 3 people got off
    num_people += 2 * 10  # Twice as many people from first stop got on

    # Third stop
    num_people -= 18  # 18 people got off
    num_people += 2  # 2 people got on

    # Return the number of people currently on the trolley
    result = num_people
    return result

print(solution())