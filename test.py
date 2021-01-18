from unittest import TestCase
from answer import solve_brute_force, solve_dp
from random import randint

solver = solve_dp


class TestProblem(TestCase):
    def test_case_simple(self):
        n = 3
        W = 100
        weight = [1, 2, 3]
        value = [1, 2, 3]

        answer = solver(n=n, W=W, weight=weight, value=value)
        self.assertEqual(answer, 6)

    def test_case_complex_1(self):
        n = 4
        W = 10
        weight = [3, 3, 6, 3]
        value = [3, 3, 6, 3]

        answer = solver(n=n, W=W, weight=weight, value=value)
        self.assertEqual(answer, 9)

    def test_case_complex_2(self):
        n = 5
        W = 10
        weight = [1, 2, 10, 2, 4]
        value = [10, 20, 100, 20, 40]

        answer = solver(n=n, W=W, weight=weight, value=value)
        self.assertEqual(answer, 100)

    def test_case_many(self):
        """
        This test judge if calculation will be finished.
        """
        n = 1000
        W = 10000
        weight = [randint(1, 1000) for i in range(n)]
        value = [randint(1, 1000) for i in range(n)]
        answer = solver(n=n, W=W, weight=weight, value=value)

        print(answer)
