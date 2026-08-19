score = [80,70,90]
min_grade = None
max_grade = None
sum_grade = 0.0
print("我的名字是：小小")
print("本次考试我的语文成绩：%d" % score[0])
print("本次考试我的数学成绩：%d" % score[1])
print("本次考试我的英语成绩：%d" % score[2])
sum_grade = score[0] + score[1] + score[2]
ave_grade = sum_grade / 3
min_grade = score.index(min(score))
max_grade = score.index(max(score))
print("本次考试我的总分是：", sum_grade)
print("本次考试我的平均分是：", ave_grade)
print("本次考试我的最高分是：", score[max_grade])
print("本次考试我的最低分是：", score[min_grade])