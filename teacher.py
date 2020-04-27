from random import choice
import numpy as np
from plot import show
from perceptron import Perceptron
from mutator import Mutator


class TeacherMut():
    def __init__(self, reals, muts=10):
        assert(len(reals) != 0)
        (w, h) = reals[0].shape
        self.reals = reals
        self.mutators = [Mutator(w, h) for _ in range(muts)]
        self.perceptron = Perceptron(w, h)

        self.buff = np.zeros_like(self.mutators[0].pattern)

    def teach_percept(self, iters=5):
        for _ in range(iters):
            self.perceptron.learn(
                choice(self.reals),
                True)
            self.perceptron.learn(
                choice(self.mutators).pattern,
                False)

    def teach_mut(self, iters=15):
        for _ in range(iters):
            for old in self.mutators:
                old.mutate(self.buff)
                new_score = self.perceptron.score(self.buff)
                old_score = self.perceptron.score(old.pattern)
                if new_score > old_score:
                    t = old.pattern
                    old.pattern = self.buff
                    self.buff = t

    def teach(self, iters=20, progress = True):
        for it in range(iters):
            if progress:
                print("{}/{}".format(it, iters))
            self.teach_percept()
            self.teach_mut()

    def reveal(self):
        show(self.perceptron.pattern)
        for x in self.mutators[0:3]:
            show(x.pattern)

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


if __name__ == "__main__":
    real = np.zeros((40, 40))
    for i in range(40):
        real[3][i] = 1
    teacher = Teacher([real], 10)
    teacher.teach(30)
    show(teacher.perceptron.pattern)
    for x in teacher.mutators:
        show(x.pattern)
