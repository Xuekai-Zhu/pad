def solution():
    """In a school, the number of participants in the 2018 Science Quiz Bowl was 150. There were 20 more than twice the number of participants in 2019 as there were in 2018. In 2020, the number of participants was 40 less than half the number of participants in 2019. How many more participants were there in 2019 than in 2020?"""
    participants_2018 = 150
    participants_2019 = 20 + 2 * participants_2018
    participants_2020 = (1/2) * participants_2019 - 40
    difference = participants_2019 - participants_2020
    result = difference
    return result

print(solution())