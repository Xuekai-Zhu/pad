def solution():
    """Billy ate 20 apples this week. On Monday, he ate 2 apples. On Tuesday, he ate twice as many as he ate the day before. He’s not sure what he ate on Wednesday. On Thursday, he ate four times as many as he ate on Friday. On Friday, he ate half of the amount he ate on Monday. How many apples did he eat on Wednesday?"""
    # Define the number of apples ate on Monday
    monday_apples = 2

    # Define the number of apples ate on Tuesday
    tuesday_apples = monday_apples * 2

    # Define the number of apples ate on Friday
    friday_apples = monday_apples / 2

    # Define the number of apples ate on Thursday
    thursday_apples = friday_apples * 4

    # Define the total number of apples ate
    total_apples = 20

    # Calculate the number of apples ate on Wednesday
    wednesday_apples = total_apples - monday_apples - tuesday_apples - thursday_apples - friday_apples

    # return the result
    result = wednesday_apples
    return result

print(solution())