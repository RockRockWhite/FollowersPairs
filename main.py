import pymysql


def main():
    # 获得电影id
    movies = []
    print("请输入俩部电影ID:")
    for cnt in range(2):
        movie_curr = input(f"{cnt + 1}:")
        movies.append(movie_curr)
    # 从数据库中读取数据
    db = pymysql.connect(host="localhost",
                         user="root",
                         password="white",
                         database="DoubanSpider")

    followers_sets = []

    for movie in movies:
        cursor = db.cursor()
        command = f"select * from t{movie}"
        cursor.execute(command)
        set_curr = set(cursor.fetchall())
        followers_sets.append(set_curr)

    # 计算重合度
    intersection = set.intersection(followers_sets[0], followers_sets[1])
    intersection_len = len(intersection)
    if len(followers_sets[0]) > len(followers_sets[1]):
        total_len = len(followers_sets[0])
    else:
        total_len = len(followers_sets[1])

    print("重合度为%.2f%%" % (intersection_len / total_len * 100))


if __name__ == '__main__':
    main()
