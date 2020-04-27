import numpy as np


def heading(f):
    assert(ord(f.read(1)) == 0)
    assert(ord(f.read(1)) == 0)
    assert(ord(f.read(1)) == 8)

    num_dims = (ord(f.read(1)))
    dims = []
    for _ in range(num_dims):
        dims.append(int.from_bytes(f.read(4), "big"))

    return dims


def parse_img(f, w, h):
    arr = []
    for _ in range(w):
        t = []
        arr.append(t)
        for _ in range(h):
            t.append(ord(f.read(1)))
    ret = np.array(arr)
    return ret


def parse(file_name):
    dat = file_name + ".dat"
    lab = file_name + ".lab"

    data_file = open(dat, 'rb')
    data_dims = heading(data_file)

    label_file = open(lab, 'rb')
    label_dims = heading(label_file)

    num = label_dims[0]

    for _ in range(num):
        label = ord(label_file.read(1))
        image = parse_img(data_file, data_dims[1], data_dims[2])
        yield (label, image)


def read_training(desired):
    for (label, img) in parse("data/train"):
        yield (img, label == desired)


def get_training(reals, fakes, desired):
    real = []
    fake = []
    for (img, des) in  read_training(desired):
        if des and reals > 0:
            real.append(img)
            reals -= 1
        elif fakes > 0:
            fake.append(img)
            fakes -= 1
        if reals == 0 and fakes == 0:
            return (real, fake)
    print("Too many requested")
    assert(False)


def get_testing(size, desired):
    if size == 0:
        return
    for (label, img) in parse("data/test"):
        size -= 1
        yield (img, label == desired)
        if size == 0:
            return


if __name__ == "__main__":
    data = parse("data/train")
    for (lab, img) in data:
        print(lab)
    # for img in imgs:
    #     show(img)
