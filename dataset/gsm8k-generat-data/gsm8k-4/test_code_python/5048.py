def solution():
    """Jessie won 3 times as many athletic awards as his buddy Scott, who won 4 awards. The best athlete at the rival high school won twice as many awards as Jessie. How many awards did the rival win?"""
    # Define the number of awards won by Scott
    scott_awards = 4

    # Calculate the number of awards won by Jessie
    jessie_awards = scott_awards * 3

    # Calculate the number of awards won by the rival
    rival_awards = jessie_awards * 2

    # return the result
    result = rival_awards
    return result

print(solution())