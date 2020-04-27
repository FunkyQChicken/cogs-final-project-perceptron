from teacher import TeacherMut
from plot import show
from teacher_van import TeacherVan
from teacher_mix import TeacherMix
from loader import get_training, get_testing


def results():
    num = 0
    (reals, fakes) = list(get_training(1000, 9000, num))
    all_test = list(get_testing(-1, num))
    test = all_test[0:1000]
    big_test = all_test[1000:]

    print(len(big_test))

    for iteration in range(5):
        teachers = [
            TeacherMut(reals, 40),
            TeacherVan(reals, fakes),
            TeacherMix(reals, fakes, 20)
            ]

        maxes = [0, 0, 0]
        overall = [None, None, None]

        for x in range(50):
            for i in range(len(teachers)):
                teacher = teachers[i]
                teachers[i]
                teacher.teach(5, False)
                (pos, fal) = teacher.score(test)
                score = pos * fal
                if score > maxes[i] and x > 30:
                    maxes[i] = score
                    overall[i] = teacher.score(big_test)
                    print("{}".format(overall))

        print("Done.")
        if iteration == 4:
            for x in teachers:
                x.reveal()


def mnist_example():
    for num in range(10):
        print(num)
        img = list(get_training(1, 0, num))[0]
        if len(img) != 0:
            img = img[0]
            show(img, "images/gen_mnist_" + str(num))

def pics_of_all_numbers():
    names = ["mut", "van", "mix"]
    for num in range(10):
        print(num)
        (reals, fakes) = list(get_training(1000, 9000, num))
        teachers = [
            TeacherMut(reals, 20),
            TeacherVan(reals, fakes),
            TeacherMix(reals, fakes, 10)]

        for (teacher, name) in zip(teachers, names):
            print(name)
            teacher.teach(40)
            teacher.save("images/gen_" + name + "_" + str(num))


mnist_example()
pics_of_all_numbers()
