# Assertionn error
#assert sum([1, 3, 5]) == 10, "Delowar sum should be"
def test_sum2():
    assert sum([2, 3, 5]) == 10, "it should be 10"

def test_sum_tuple():
    assert sum((1, 3, 5)) == 10, "it ahould be 10"

if __name__ == '__main__':
    test_sum2()
    test_sum_tuple()
    print("Everything is correct")
