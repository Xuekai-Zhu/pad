def solution():
     """Noah is a painter. He paints pictures and sells them at the park. He charges $60 for a large painting and $30 for a small painting. Last month he sold eight large paintings and four small paintings. If he sold twice as much this month, how much is his sales for this month?"""
     large_painting_price = 60
     small_painting_price = 30
     sales_last_month = 8 * large_painting_price + 4 * small_painting_price
     sales_this_month = 2 * sales_last_month
     result = sales_this_month
     return result

print(solution())