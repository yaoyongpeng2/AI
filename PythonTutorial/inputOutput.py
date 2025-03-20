#7.1. Fancier Output Formatting
yes_votes = 42_572_654#数字中使用 _ 作为分隔符，提高可读性，不影响数值。编译时会自动忽略 _，等同于 42572654。
total_votes = 85_705_149#t同上
percentage = yes_votes / total_votes
#: 是 ​格式说明符，
# - 表示左对齐，9 表示总宽度为 9 字符。yes_votes 是数字，会先转换为字符串再对齐。
#2.2%的第一个2是​最小总宽度，表示整个字段（包括数字和 % 符号）至少占 2 字符宽度。
# 但 ​由于百分比数值通常超过 2 字符宽度，这个参数在此场景下 ​实际会被忽略。
# .2 ​仅控制小数点后的位数，与整数部分无关。
# %将小数转换为百分比格式（自动乘以 100，并添加 % 符号）
print("{:-9} YES votes  {:2.2%}".format(yes_votes, percentage))
print(f"{yes_votes:-9} YES votes  {percentage:2.2%}")#同上