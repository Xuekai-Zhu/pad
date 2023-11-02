def solution():
    # Calculate the number of pencils Jeff donated
    donated_jeff = 0.3 * 300

    # Calculate the number of pencils Jeff has left
    left_jeff = 300 - donated_jeff

    # Calculate the number of pencils Vicki had
    pencils_vicki = 2 * 300

    # Calculate the number of pencils Vicki donated
    donated_vicki = 0.75 * pencils_vicki

    # Calculate the number of pencils Vicki has left
    left_vicki = pencils_vicki - donated_vicki

    # Calculate the total number of pencils remaining
    total_remaining = left_jeff + left_vicki

    result = total_remaining
    return result

print(solution())