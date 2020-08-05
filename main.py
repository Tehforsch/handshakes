from typing import List, Tuple, Iterator
import itertools


def validSolution(N: int, S: List[set]) -> bool:
    return all(S[i] == set(range(N)) for i in range(N))


def getS(N: int, exchanges: Iterator[Tuple[int, int]]) -> List[set]:
    S = [set([i]) for i in range(N)]
    for j1, j2 in exchanges:
        S = [S[j1] | S[j2] if (i == j1) or (i == j2) else S[i] for i in range(N)]
    return S


def hasSolution(N: int, n: int) -> bool:
    allPeople = range(N)
    possibleExchanges = list(itertools.combinations(allPeople, 2))
    exchangeSequences = itertools.product(*(possibleExchanges for _ in range(n)))
    # print(list(exchangeSequences))
    for swaps in exchangeSequences:
        if validSolution(N, getS(N, swaps)):
            print(N, swaps)
            return True
    return False


def h(N: int) -> int:
    for n in range(1, 2 * N - 3):
        # numCombinations = N ** (2 * n)
        # print(f"Checking {N}, {n} ({numCombinations})")
        if hasSolution(N, n):
            return n
    return 2 * N - 3


# print(hasSolution(4, 2))
# for n in range(5):
# print(hasSolution(3, n))
for N in range(2, 10):
    print(N, h(N))
# print(validSolution(4, getS(4, [(0, 1), (2, 3), (0, 3), (1, 2)])))
