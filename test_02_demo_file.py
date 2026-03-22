# Any pytest file should start with test_ or ends with _test
# Pytest function names should start with test

def test_assert():
    msg = "hello"
    assert msg == "h1", "Test failed because string did not matched"

