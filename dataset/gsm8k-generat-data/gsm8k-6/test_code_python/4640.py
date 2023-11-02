def solution():
    # Calculate the total number of pencils Teresa has
    total_pencils = 14 + 35  # 14 colored pencils and 35 black pencils
    total_given_pencils = total_pencils - 10  # Teresa keeps 10 pencils for herself

    # Calculate the number of pencils each sibling gets
    pencils_per_sibling = total_given_pencils // 3  # divide equally among three siblings

    result = pencils_per_sibling
    return result

print(solution())