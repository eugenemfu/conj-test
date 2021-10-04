import numpy as np
from scipy.stats import rankdata


def conj_test(points: list):

    y = np.array([p[1] for p in sorted(points)])

    n = len(y)
    p = int(round(n / 3))

    ranks = rankdata(y)

    r1 = sum(ranks[:p])
    r2 = sum(ranks[-p:])

    diff = int(round(r2 - r1))
    stderr = int(round((n + 0.5) * np.sqrt(p / 6)))
    conj = round((r2 - r1) / (p * (n - p)), 2)
    
    return diff, stderr, conj


if __name__ == '__main__':

    with open('in.txt') as f:
        points = f.readlines()

    try:
        for i in range(len(points)):
            points[i] = tuple(map(float, points[i].split()))
            assert len(points[i]) == 2, "wrong input format."
    except ValueError:
        raise ValueError('wrong input format.')
        
    ans = conj_test(points)

    with open('out.txt', 'w') as f:
        f.write(f'{ans[0]} {ans[1]} {ans[2]}\n')

