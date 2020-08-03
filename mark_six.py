import random

error = '輸入錯誤'


def lottery():  # 開獎模塊
    table = list(range(1, 50))
    random.shuffle(table)
    drawn0 = table[:6]
    drawn0.sort()
    return [tuple(drawn0), table[6]]  # 第七個是‘特別號碼’


def rand_choose():  # 機選模塊
    table = list(range(1, 50))
    random.shuffle(table)
    choice0 = table[:6]
    choice0.sort()
    return tuple(choice0)  # 選六個


def choose():  # 選擇號碼
    count = 0
    choice0 = []
    while True:
        decision = input('你想手動選擇一組六合彩號碼嗎？[y/n]:')
        if decision == 'n':
            choice0 = rand_choose()
            print('爲你隨機選擇一個組合：', choice0)
            break
        elif decision == 'y':
            while count < 6:
                number = input('請輸入一個數字(1-49)：')  # 手選模塊
                try:  # 檢測輸入是否合法
                    int(number)
                except ValueError:
                    print(error)
                    continue
                if int(number) not in range(1, 50) or int(number) in choice0:
                    print(error)
                    continue
                choice0.append(int(number))
                count += 1
            choice0.sort()
            print('你選擇了一個組合：', tuple(choice0))
            break
        else:
            print(error)
            continue
    return tuple(choice0)


def prize():  # 判斷中獎模塊
    count = 0
    extra = False
    for each in range(0, 6):
        if chosen[each] in drawn[0]:
            count += 1
        if chosen[each] == drawn[1]:
            extra = True
    if count == 6:
        prize0 = '1st'
    elif count == 5 and extra:
        prize0 = '2nd'
    elif count == 5:
        prize0 = '3rd'
    elif count == 4 and extra:
        prize0 = '4th'
    elif count == 4:
        prize0 = '5th'
    elif count == 3 and extra:
        prize0 = '6th'
    elif count == 3:
        prize0 = '7th'
    else:
        prize0 = 'none'
    return prize0


class User:

    def __init__(self, name='', total_profit=0, profit=None, balance=1000, chosen_numbers=None, prize=None):
        self.name = name
        self.profit = profit
        self.t_profit = total_profit
        self.balance = balance
        self.cn = chosen_numbers
        self.prize = prize

    def detail(self):
        print('==============================DETAILS==============================')
        print('{0:^5} {1:<15} {2:<25} {3:<15} {4:<20}'.format('#', 'name', 'chosen numbers', 'prize', 'profit', ))
        for time in range(int(times)):
            print('{0:^5} {1:<15} {2:<25} {3:<15} {4:<20}'.format(time + 1, self.name if time == 0 else '',
                                                                  str(self.cn[time]), self.prize[time],
                                                                  self.profit[time]))
        print('{0:^5} {1:<15} {2:<25} {3:<15} {4:<20}'.format('#', '', 'lottery result', 'total profit', 'balance'))
        print('{0:^5} {1:<15} {2:<15} {3:<15} {4:<20}'.format('#', '', str(drawn), self.t_profit, self.balance))
        print('===================================================================')

    def detail_bot(self):
        print('=========================DETAILS=========================')
        print('{0:^5}{1:<15}{2:<25}{3:<15}'.format('#', 'name', 'chosen number', 'prize'))
        print('{0:^5}{1:<15}{2:<25}{3:<15}'.format('#', self.name, str(self.cn), self.prize))
        print('=========================================================')

    def change(self, total_profit=0, profit=None, chosen_numbers=None, prize=None):
        self.profit = profit
        self.t_profit = total_profit
        self.balance += total_profit
        self.cn = chosen_numbers
        self.prize = prize


# ==========================================================================================
name = input('新建一個昵稱：')
player = User(name)  # 玩家初始化
print('你好{0}！\n歡迎游玩六合彩模擬器\n你的初始基金為{1}元\n祝你好運！'.format(player.name, player.balance))
pool = 0

while True:
    count = 0  # 總票數
    population = random.randint(2000000, 4000000)
    dict0 = {'1st': 0, '2nd': 0, '3rd': 0, '4th': 0, '5th': 0, '6th': 0, '7th': 0, 'none': 0}  # 獲獎次數統計
    dict1 = {'1st': 0, '2nd': 0, '3rd': 0, '4th': 9600, '5th': 640, '6th': 320, '7th': 40, 'none': 0}  # 獲獎金額統計
    drawn = lottery()  # 開獎
    while True:
        times = input('輸入你想要下的注數（每注10元）：')
        try:  # 檢測輸入是否合法
            int(times)
        except ValueError:
            print(error)
            continue
        if int(times) <= 0:
            print(error)
            continue
        elif 10 * int(times) > player.balance:
            print('餘額不足')
        else:
            break
    chosens = []
    awards = []
    for time in range(int(times)):  # 人的中獎判定
        chosen = choose()  # 選一組號碼
        chosens.append(chosen)
        awards.append(prize())  # 比對得獎
        dict0[awards[time]] += 1  # 得獎計數
        count += 1  # 人購買注數計數
    for i in range(population):  # bot的中獎判定及結算
        for j in range(random.randint(1, 3)):
            chosen = rand_choose()  # 隨機生成號碼
            award = prize()  # 比對得獎
            dict0[award] += 1  # 得獎計數
            bot = User('bot{}'.format(i), chosen_numbers=chosen, prize=award)  # 每個bot初始化
            bot.detail_bot()
            count += 1  # bot購買注數計數
    pool += count * 5.4
    pool -= dict0['7th'] * 40 + dict0['6th'] * 320 + dict0['5th'] * 640 + dict0['4th'] * 9600  # 減去四五六七等獎獎金
    if dict0['3rd'] != 0:
        dict1['3rd'] = pool * .4 / dict0['3rd']
    if dict0['2nd'] != 0:
        dict1['2nd'] = pool * .15 / dict0['2nd']
    if dict0['1st'] != 0:
        dict1['1st'] = pool * .45 / dict0['1st']
    if dict1['1st'] * dict0['1st'] < 8000000 and dict0['3rd'] != 0:  # 一等獎獎池不得少於八百萬
        temp = 8000000 - dict1['1st'] * dict0['1st']
        dict1['1st'] = 8000000
        dict1['2nd'] -= temp * .25 / dict0['2nd']  # 獎金動態調整
        dict1['3rd'] -= temp * .45 / dict0['3rd']  # 獎金動態調整
    if dict1['1st'] < dict1['2nd'] * 2 and dict0['2nd'] != 0:  # 一等獎不得少於二等獎的兩倍
        temp = (dict1['2nd'] * 2 - dict1['1st']) * dict0['2nd']
        dict1['2nd'] = dict1['1st'] / 2
        dict1['3rd'] += temp / dict0['3rd']
    if dict1['2nd'] < dict1['3rd'] * 2 and dict0['1st'] != 0:  # 二獎不得少於三等獎的兩倍
        temp0 = (dict1['3rd'] * 2 - dict1['2nd']) * dict0['3rd']
        dict1['3rd'] = dict1['2nd'] / 2  # 獎金動態調整
        pool += temp0  # 補回差額給下一輪獎池
    pool -= dict0['3rd'] * dict1['3rd'] + dict0['2nd'] * dict1['2nd'] + dict0['1st'] * dict1['1st']  # 減去一二三等獎獎金
    print(dict0)
    print(dict1)
    money = []
    total_money = 0
    for time in range(int(times)):  # 人的結算判定
        money.append(dict1[awards[time]])
        total_money += money[time]
    player.change(total_profit=total_money - int(times) * 10, profit=money, chosen_numbers=chosens, prize=awards)
    player.detail()
    if player.balance <= 10:
        print('你破產了')
        print('江湖險、賭博更險。春冰薄、贏面更薄。\n黃蓮苦、輸錢更苦。登山難、借錢更難。\n知其難、避其險、耐其苦、戒其賭、可處世矣')
        break

input()
