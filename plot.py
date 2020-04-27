import pylab as plt


def show(mat, save_loc=False):
    (rows, cols) = mat.shape
    plt.imshow(mat, cmap='hot', aspect=(cols/rows))
    if save_loc:
        plt.savefig(save_loc)
    else:
        plt.show()
