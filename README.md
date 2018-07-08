# ItemCollab
ItemCollab是一个用于实现个性化推荐的Python软件包。

它包括数据处理、物品推荐、质量评价三个模块。数据处理模块实现数据导入、稀疏度分析和训练集划分功能；物品推荐模块实现了目前主流的几种推荐算法；质量评价模块实现对推荐质量的图表展示功能。ItemCollab扩展性好，便于引用，可帮助用户构建自己的个性化推荐系统


ml-100k.zip是本软件包内置的数据集，用户可将其下载解压后作为示例程序的数据输入

cosine_similarity.py是一个调整的余弦相似度模型的示例

recommendations.py是本软件包的主体程序，其运行示例如下：

r = recommender(users2)
r.computeDeviations()
g = users2["Ben"]
print(r.slopeOneRecommendations(g))
