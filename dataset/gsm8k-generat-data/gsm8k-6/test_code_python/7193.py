def solution():
    # Find out the number of questions the second student got right
    num_right = 40 - 3 # the second student got 3 questions wrong out of 40 total questions

    # Find the minimum score Hannah needs to beat
    min_score = max((95/100)*100, (num_right/40)*100) # take the maximum of the percentages for the two students
    # This will give the minimum score Hannah needs to beat to get the highest grade in the class

    # Find out the number of questions Hannah needs to get right to achieve the minimum score
    num_right_to_beat = (min_score/100)*40 # convert the minimum score to a percentage and multiply by the total number of questions

    # Round up to the nearest whole number
    num_right_to_beat = int(num_right_to_beat + 0.5)

    result = num_right_to_beat
    return result

print(solution())