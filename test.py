# code to check max number between two numbers
def max_number(a, b):
    if a > b:
        return a
    else:
        return b

# Q: how to test this function?
def test_max_number():
    assert max_number(10, 5) == 10
    assert max_number(5, 10) == 10
    assert max_number(-1, -5) == -1
    assert max_number(0, 0) == 0


# how to make agent run this test?
if __name__ == "__main__":
    test_max_number()
    print("All tests passed!")  