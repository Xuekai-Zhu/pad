def solution():
    total_students = 1000
    male_students = 3/5 * total_students
    female_students = 2/5 * total_students
    male_basket_likers = 2/3 * male_students
    female_basket_likers = 1/5 * female_students
    total_basket_likers = male_basket_likers + female_basket_likers
    percent_dislike_basket = (total_students - total_basket_likers)/ total_students
    
    return percent_dislike_basket

print(solution())