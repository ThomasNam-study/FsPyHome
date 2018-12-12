import matplotlib.pyplot as plt

days = list(range(1, 31 + 1))

first_mon_h = [4, 2, 0, -1, 2, 3, 3, 4, -1, -5, -7, -5, -1, 5, 8, 7, 9, 5, 6, 7, 6, 4, -5, -11, -10, -11, -4, -1, -5, -1, 0]
first_mon_l = [-5, -6, -7, -9, -6, -7, -6, -3, -6, -11, -14, -15, -7, -4, 0, 0, 2, -1, -3, -2, -4, -9, -15, -16, -16, -18, -16, -10, -12, -11, -6]

#plt.rcParams['font.family'] = 'KoreanHHM'

plt.plot(days, first_mon_h, 'ro-', days, first_mon_l, 'bo-')
plt.xlabel("일")
plt.ylabel("온도")
plt.title("1월 온도표")
plt.show()