import numpy as np


class Perceptron:
    def __init__(self, w, h):
        self.pattern = np.zeros((w, h))

    def match(self, img):
        score = self.score(img)
        return score > 0.0

    def score(self, matt):
        return sum(map(
            lambda x : x[0] * x[1],
            zip(
            np.nditer(self.pattern),
            np.nditer(matt)
        )))

    def learn(self, matt, real):
        score = self.score(matt)
        if real and score <= 0:
            self.enforce(matt)
            return -abs(score)
        elif not real and score >= 0:
            self.reject(matt)
            return -abs(score)
        return abs(score)

    def enforce(self, matt):
        pattern = np.nditer(self.pattern, op_flags=['readwrite'])
        offset = np.nditer(matt)
        for (patt, off) in zip(pattern, offset):
            patt[...] += off

    def reject(self, matt):
        pattern = np.nditer(self.pattern, op_flags=['readwrite'])
        offset = np.nditer(matt)
        for (patt, off) in zip(pattern, offset):
            patt[...] -= off




if __name__ == "__main__":
    perc = Perceptron(3,3)
    patt = np.ones((3,3))
    assert(perc.score(patt) == 0.0)
    perc.learn(patt, True)
    assert(perc.score(patt) == 9.0)
