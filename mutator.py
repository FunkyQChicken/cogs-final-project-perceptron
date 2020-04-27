import numpy as np
from random import randint, random


class Mutator:
    def __init__(self, w, h):
        self.pattern = np.zeros((w, h), dtype='u8')

    def matt(self):
        self.pattern

    def mutate(self, buff, odds = 0.10, rng = 10):
        buff_it = np.nditer(buff, op_flags=['readwrite'])
        patt_it = np.nditer(self.pattern)
        for (b, p) in zip(buff_it, patt_it):
            if random() < odds:
                new_p = randint(p - rng, p + rng)
                b[...] = max(0.0, min(new_p, 255.0))
            else:
                b[...] = p


if __name__ == "__main__":
    mut = Mutator(3, 3)
    print(mut.pattern)
    new  = mut.mutate().mutate().mutate()
    print(new.pattern)
