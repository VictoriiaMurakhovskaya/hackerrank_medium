from unittest import TestCase, main
from equation import solve


class TestEquation(TestCase):
    def test_1(self):
        eqn = '2x=3'
        self.assertEqual(solve(eqn), 1.5)

    def test_2(self):
        eqn = '-2x=3'
        self.assertEqual(solve(eqn), -1.5)

    def test_3(self):
        eqn = '3=2x'
        self.assertEqual(solve(eqn), 1.5)

    def test_4(self):
        eqn = '-3=2x'
        self.assertEqual(solve(eqn), -1.5)

    def test_5(self):
        eqn = '-2x=-3'
        self.assertEqual(solve(eqn), 1.5)

    def test_6(self):
        eqn = '-3=-2x'
        self.assertEqual(solve(eqn), 1.5)

    def test_7(self):
        eqn = 'x=-x'
        self.assertEqual(solve(eqn), 0)

    def test_8(self):
        eqn = 'x=x'
        self.assertEqual(solve(eqn), 'NO')

    def test_9(self):
        eqn = '2=2'
        self.assertEqual(solve(eqn), 'NO')

    def test_10(self):
        eqn = '2=3'
        self.assertEqual(solve(eqn), 'NO')

    def test_11(self):
        eqn = '2x=3x'
        self.assertEqual(solve(eqn), 0)

    def test_12(self):
        eqn = '0=0'
        self.assertEqual(solve(eqn), 'NO')

    def test_13(self):
        eqn = '2x+1=0'
        self.assertEqual(solve(eqn), -0.5)

    def test_14(self):
        eqn = '-2x+1=0'
        self.assertEqual(solve(eqn), 0.5)

    def test_15(self):
        eqn = '-2x+1=-0'
        self.assertEqual(solve(eqn), 0.5)

    def test_16(self):
        eqn = '0=2x-4'
        self.assertEqual(solve(eqn), 2)

    def test_17(self):
        eqn = '-0=2x-4'
        self.assertEqual(solve(eqn), 2)

    def test_18(self):
        eqn = '2x+3=2x+3'
        self.assertEqual(solve(eqn), 'NO')

    def test_19(self):
        eqn = '-2x+2=-2x+3'
        self.assertEqual(solve(eqn), 'NO')

    def test_20(self):
        eqn = '-2x+3=2x+3'
        self.assertEqual(solve(eqn), 0)

    def test_21(self):
        eqn = '3-2x=-1'
        self.assertEqual(solve(eqn), 2)

    def test_22(self):
        eqn = '-3+2x=4x-1'
        self.assertEqual(solve(eqn), -1)

    def test_23(self):
        eqn = '-2x+3=2x-3'
        self.assertEqual(solve(eqn), 1.5)

    def test_24(self):
        eqn = '-12x+18=-30+12x'
        self.assertEqual(solve(eqn), 2)

    def test_25(self):
        eqn = '1000x=1000x'
        self.assertEqual(solve(eqn), 'NO')

    def test_26(self):
        eqn = '0x=1000'
        self.assertEqual(solve(eqn), 'NO')

    def test_27(self):
        eqn = '3x-4+4x-3=0'
        self.assertEqual(solve(eqn), 1)


if __name__ == '__main__':
    main()