import pytest

"""  IN Terminal pytest (filename- like test_markers) -m(mean markers) markers_name(login-ex) -v(verbose - its give even more info about testcase """
def test_m1():
    a = 2
    b = 3
    assert a == b

def test_m2():
    assert True

def test_login():
    assert "admin" == "admin"
