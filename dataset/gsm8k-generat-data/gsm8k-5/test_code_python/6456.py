def solution():
    rent = 1200  # Rent for the year is $1200
    mrs_share = rent * 0.3  # Mrs. McPherson agreed to raise 30% of the rent
    mr_share = rent - mrs_share  # Mr. McPherson needs to raise the remaining amount

    result = mr_share
    return result

print(solution())