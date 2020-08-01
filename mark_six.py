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
    decision = input('你想手動選擇一組六合彩號碼嗎？[Y/N]:')
    if decision == 'N':
        choice0 = rand_choose()
        print('爲你隨機選擇一個組合：', choice0)
    elif decision == 'Y':
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
    balance = 1000

    def __init__(self, name='', profit=0, balance=1000, chosen_numbers=(), prize=''):
        self.name = name
        self.profit = profit
        self.balance = balance
        self.cn = chosen_numbers
        self.prize = prize

    def detail(self):
        print('=========================DETAILS=========================')
        print('name:', self.name)
        print('chosen numbers:', self.cn)
        print('prize:', self.prize)
        print('=========================================================')

    def detail_bot(self):
        print('=========================DETAILS=========================')
        print('name:', self.name)
        print('chosen numbers:', self.cn)
        print('prize:', self.prize)
        print('=========================================================')


# ============================================================================
name = input('新建一個昵稱：')
player = User(name)  # 玩家初始化

while True:
    population = random.randint(2000000, 4000000)
    dict0 = {'1st': 0, '2nd': 0, '3rd': 0, '4th': 0, '5th': 0, '6th': 0, '7th': 0, 'none': 0}  # 獲獎次數統計
    drawn = lottery()  # 開獎
    while True:
        times = input('輸入你想要下的注數（每注十元）：')
        try:  # 檢測輸入是否合法
            int(times)
        except ValueError:
            print(error)
            continue
        if int(times) <= 0:
            print(error)
            continue
        elif 10 * int(times) >= player.balance:
            print('餘額不足')
        else:
            break
    for time in range(int(times)):  # 人的中獎判定以及結算
        chosen = choose()  # 選一組號碼
        award = prize()  # 比對得獎
        dict0[award] += 1  # 得獎計數
    for i in range(population):  # bot的中獎判定及結算
        for j in range(random.randint(1, 3)):
            chosen = rand_choose()  # 隨機生成號碼
            award = prize()  # 比對得獎
            dict0[award] += 1  # 得獎計數
            bot = User('bot{}'.format(i), chosen_numbers=chosen, prize=award)  # 每個bot初始化
            bot.detail_bot()

    print(dict0)
    break
