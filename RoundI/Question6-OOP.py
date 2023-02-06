class TestMath:
    def test_add(self, x, y):
     return x + y

    def test_subtract(self, x, y):
        x - y

    def test_milutiply(self, x, y):
        return x * y

# Create a TestMath object
my_tm = TestMath()

x = 10
y = 10

my_tm.test_add(x, y)
my_tm.test_subtract(x, y)
my_tm.test_milutiply(x, y)