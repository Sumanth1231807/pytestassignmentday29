import pytest_program
import pytest

@pytest.mark.xfail
@pytest.mark.parametrize("x,result",[(154,True),(372,True),(400,True),(408,False)])
def test_armstrong(x,result):
    armstrong=pytest_program.armstrong(x)
    assert armstrong == result

@pytest.mark.skip(reason="not necessary")
@pytest.mark.parametrize("x,result",[(21,True),(80,True),(32,True),(56,False)])
def test_Divisible_or_not(x,result):
    divisible=pytest_program.Divisible_or_not(x)
    assert divisible == result

@pytest.mark.xfail
@pytest.mark.parametrize("x,y,z,result",[(2,8,2,1),(1,1,2,19)])
def test_Smallest_of_threenum(x,y,z,result):
    smallest=pytest_program.Smallest_of_threenum(x,y,z)
    assert smallest == result

@pytest.mark.xfail
@pytest.mark.parametrize("x,result",[(4,"even"),(7,"odd"),(6,"even")])
def test_check_even_odd(x,result):
    oddeven=pytest_program.check_even_odd(x)
    assert oddeven == result

@pytest.mark.xfail
@pytest.mark.parametrize("my_str,result",[("lol",True),("sing",False),("prince",True)])
def test_palindrome(my_str,result):
    palindrome=pytest_program.palindrome(my_str)
    assert palindrome == result