from sys import argv


class Point:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y


def on_point(point, figure):
    x = 0
    for i in figure:
        if point.X == i.X and point.Y == i.Y:
            x = 1
    return x


def rectangle_square(a, b, c):
    return abs(a.X*(b.Y - c.Y) +  b.X*(c.Y - a.Y) + c.X*(a.Y - b.Y) ) / 2.0


def main():
    figure_file = argv[1]
    points_file = argv[2]

    figure_list = []
    points_list = []

    with open (figure_file) as figure_file_obj:
        figure_data = figure_file_obj.read().splitlines()
        
    for point in figure_data:
        x_coord = float(point[point.find(' '):])
        y_coord = float(point[:point.find(' ')])
        figure_list.append(Point(x_coord, y_coord))

    with open (points_file) as points_file_obj:
        points_data = points_file_obj.read().splitlines()

    for point in points_data:
        x_coord = float(point[point.find(' '):])
        y_coord = float(point[:point.find(' ')])
        points_list.append(Point(x_coord, y_coord))
    
    figure_square = rectangle_square(figure_list[0], figure_list[1], figure_list[2]) + rectangle_square(figure_list[1], figure_list[2], figure_list[3])

    for point in points_list:
        if on_point(point, figure_list) == 1:
            print('0')
            continue
        point_square = rectangle_square(point, figure_list[0], figure_list[1]) + rectangle_square(point, figure_list[1], figure_list[2]) + rectangle_square(point, figure_list[2], figure_list[3]) + rectangle_square(point, figure_list[3], figure_list[0])
        if (rectangle_square(point, figure_list[0], figure_list[1]) == 0 or rectangle_square(point, figure_list[1], figure_list[2]) == 0 or rectangle_square(point, figure_list[2], figure_list[3]) == 0 or rectangle_square(point, figure_list[3], figure_list[0]) == 0) and point_square == figure_square:
            print('1')
            continue
        elif point_square == figure_square:
            print('2')
        else:
               print('3')


if __name__ == "__main__":
    main()
