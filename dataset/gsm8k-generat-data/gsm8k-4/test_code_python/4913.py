def solution():
    """In a school, the number of participants in the 2018 Science Quiz Bowl was 150. There were 20 more than twice the number of participants in 2019 as there were in 2018. In 2020, the number of participants was 40 less than half the number of participants in 2019. How many more participants were there in 2019 than in 2020?"""
    # Define the number of participants in 2018
    participants_2018 = 150

    # Calculate the number of participants in 2019
    participants_2019 = 2 * participants_2018 + 20

    # Calculate the number of participants in 2020
    participants_2020 = 0.5 * participants_2019 - 40

    # Calculate the difference in number of participants between 2019 and 2020
    difference = participants_2019 - participants_2020

    # return the result
    result = difference
    return result

print(solution())