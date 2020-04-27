from random import choice
from plot import show
from perceptron import Perceptron


class TeacherVan():
    def __init__(self, reals, fakes):
        assert(len(reals) != 0)
        assert(len(fakes) != 0)
        (w, h) = reals[0].shape
        self.reals = reals
        self.fakes = fakes
        self.perceptron = Perceptron(w, h)

    def teach_percept(self, iters=5):
        for _ in range(iters):
            self.perceptron.learn(
                choice(self.reals),
                True)
            self.perceptron.learn(
                choice(self.fakes),
                False)

    def teach(self, iters=20, progress = True):
        for it in range(iters):
            if progress:
                print("{}/{}".format(it, iters))
            self.teach_percept()

    def reveal(self):
        show(self.perceptron.pattern)

    def save(self, prefix):
        show(self.perceptron.pattern, prefix)

    def score(self, test):
        num_desired = 0
        num_undesired = 0
        correct_desired = 0
        correct_undesired = 0
        for (img, desired) in test:
            match = self.perceptron.match(img)
            if desired:
                if match:
                    correct_desired += 1
                num_desired += 1
            else:
                if not match:
                    correct_undesired += 1
                num_undesired += 1

        return (correct_desired/num_desired, correct_undesired/num_undesired)
