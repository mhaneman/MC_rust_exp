import MC_sim
import time
import random
import math
import matplotlib.pyplot as plt


def part_a():
    rand_vals = MC_sim.gen_rand_vals()
    print(rand_vals)


def part_b():
    iterations = [100, 10_000, 100_000, 1_000_000, 100_000_000]
    sims_of_pi = [MC_sim.gen_pi(i) for i in iterations]
    print(sims_of_pi)


def gen_pi(NT):
    Nc = 0
    for _ in range(1, NT):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if math.sqrt(x**2 + y**2) <= 1:
            Nc += 1

    return 4 * Nc / NT


def gen_pi_typed(NT: int):
    Nc: int = 0
    for _ in range(1, NT):
        x: float = random.uniform(-1, 1)
        y: float = random.uniform(-1, 1)
        if math.sqrt(x**2 + y**2) <= 1:
            Nc += 1
    return 4 * Nc / NT


def part_c():
    NT = [100, 10_000, 100_000, 1_000_000, 100_000_000]

    rust_t = []
    typed_t = []
    raw_t = []

    for i in NT:
        print("NT = ", i)

        start = time.time()
        sim_of_pi = MC_sim.gen_pi(i)
        t = time.time() - start
        rust_t.append(t)
        print("rust -> ", sim_of_pi, t)

        start = time.time()
        sim_of_pi = gen_pi_typed(i)
        t = time.time() - start
        typed_t.append(t)
        print("python3 typed ->", sim_of_pi, t)

        start = time.time()
        sim_of_pi = gen_pi(i)
        t = time.time() - start
        raw_t.append(t)
        print("python3 ->", sim_of_pi, t)

        print("\n\n")

    plt.plot([str(i) for i in NT], rust_t)
    plt.plot([str(i) for i in NT], typed_t)
    plt.plot([str(i) for i in NT], raw_t)
    plt.show()


part_c()
