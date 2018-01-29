import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # generate path coordinates
    rw = RandomWalk(5000)
    rw.fill_walk()

    # set size of plot's window
    plt.figure(figsize=(10, 6))

    # set counter for every step (chronology)
    point_numbers = list(range(rw.num_points))

    # build path
    plt.plot(rw.x_values
                , rw.y_values
                , linewidth=1
                )

    # emphasise start and end-points.
    plt.scatter(0, 0, c='green', s = 10)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=10)

    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()