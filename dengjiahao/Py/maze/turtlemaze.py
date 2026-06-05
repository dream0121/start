import os
import turtle

#把 TXT 转换为 二维列表
def get_map(filename):
    with open(filename, "r") as f:
        fl = f.readlines()
    maze_list = []
    for line in fl:
        line = line.strip()
        line_list.split(" ")
        maze_list.append(line_list)
    return maze_list


if __name__ == "__main__":
    turtle.title(gametitle)
    turtle.setup(700, 520)
    gametitle = "小海龟挑战大迷宫"
    txt_path = os.path.join(os.path.dirname(__file__), "map", "map1.txt")
    # 获取当前py文件所在文件夹
    base_path = os.path.dirname(__file__)
    # 拼接图片完整路径
    img_path = os.path.join(base_path, "image", "start.png")
    turtle.bgpic(img_path)
    turtle.colormode(255)
# level = turtle.numinput("选择难度", "请输入1-3", 1, 1, 3)
# levelinit()

    turtle.done()
