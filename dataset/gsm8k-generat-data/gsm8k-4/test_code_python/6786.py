def solution():
    """The world record for longest fingernails is 26 inches. Sandy, who just turned 12 this month, has a goal for tying the record. Her fingernails are 2 inches long. Her fingernails grow at a rate of one-tenth of an inch per month. How old will she be when she achieves the world record?"""
    # Define the target length of fingernails
    target_length = 26

    # Define the initial length of Sandy's fingernails
    initial_length = 2

    # Define the growth rate of Sandy's fingernails
    growth_rate = 0.1

    # Define the initial age of Sandy
    age = 12

    # Calculate the number of months it will take to reach the target length
    months = (target_length - initial_length) / growth_rate

    # Calculate the age at which Sandy will achieve the world record
    future_age = age + months/12

    result = round(future_age)
    return result

print(solution())