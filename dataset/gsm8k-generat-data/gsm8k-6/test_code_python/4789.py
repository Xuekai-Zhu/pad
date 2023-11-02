def solution():
    # Calculate the total pounds of ground beef Maurice purchased
    total_pounds = 5 * 4  # 4 packages of 5-pound ground beef

    # Calculate the number of 2-pound burgers Maurice can make
    num_burgers = total_pounds // 2  # integer division, round down if necessary

    # Maurice needs 1 burger for himself, so he can invite num_burgers + 1 people
    num_people = num_burgers + 1

    result = num_people
    return result

print(solution())