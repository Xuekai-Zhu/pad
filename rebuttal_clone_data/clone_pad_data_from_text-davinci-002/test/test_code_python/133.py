def solution():
     
     normal_subscription_price = 34
     number_of_issues = 18 * 2
     normal_price_per_issue = normal_subscription_price / number_of_issues
     promotional_price_per_issue = normal_price_per_issue - 0.25
     promotional_subscription_price = promotional_price_per_issue * number_of_issues
     difference_in_price = normal_subscription_price - promotional_subscription_price
     result = difference_in_price
     return result

print(solution())