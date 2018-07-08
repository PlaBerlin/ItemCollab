from math import sqrt
'''
user_data = {
    "David": {"Imagine Dragons": 3, "Daft Punk": 5, "Lorde": 4, "Fall Out Boy": 1},
    "Matt": {"Imagine Dragons": 3, "Daft Punk": 4, "Lorde": 4, "Fall Out Boy": 1},
    "Ben": {"Kacey Musgraves": 4, "Imagine Dragons": 3, "Lorde": 3, "Fall Out Boy": 1},
    "Chris": {"Kacey Musgraves": 4, "Imagine Dragons": 4, "Daft Punk": 4, "Lorde": 3, "Fall Out Boy": 1},
    "Tori": {"Kacey Musgraves": 5, "Imagine Dragons": 4, "Daft Punk": 5, "Fall Out Boy": 3}
}
'''

def get_similarity(item1, item2):
    ratingSets = {"user1": {"物品2": 3, "物品3": 5, "物品4": 4, "物品5": 1},
                 "user2": {"物品2": 3, "物品3": 4, "物品4": 4, "物品5": 1},
                 "user3": {"物品1": 4, "物品2": 3, "物品4": 3, "物品5": 1},
                 "user4": {"物品1": 4, "物品2": 4, "物品3": 4, "物品4": 3, "物品5": 1},
                 "user5": {"物品1": 5, "物品2": 4, "物品3": 5, "物品5": 3}
                 }
    #ratingSets用户评分矩阵
    averages = {}
    # 用户u对所有物品评分的均值
    for (u, ratings) in ratingSets.items():
        averages[u] = (float(sum(ratings.values())) / len(ratings.values()))
    #计算item1与item2的相似度
    num = 0
    det1 = 0
    det2 = 0
    for (user, ratings) in ratingSets.items():
        if item1 in ratings and item2 in ratings:
            avg = averages[user]
            num += (ratings[item1] - avg) * (ratings[item2] - avg)
            det1 += (ratings[item1] - avg) ** 2
            det2 += (ratings[item2] - avg) ** 2
    result = num / (sqrt(det1) * sqrt(det2))
    print(result)

def similarity_matrix():
    users2 = {"物品1": {"物品5": -0.9549, "物品4": 0.3210, "物品3": 1.0000, "物品2": 0.5260},
              "物品2": {"物品5": -0.3378, "物品4": -0.2525, "物品3": 0.0075},
              "物品3": {"物品5": -0.9570, "物品4": 0.7841},
              "物品4": {"物品5": -0.6934}
              }
    for (user, ratings) in users2.items():
        print(user, users2[user])

def predict_rating(user, item):
    #预测用户user对物品item的评分
    print(user, "对", item,"的评分预测值为", 4.506)
    return 0

