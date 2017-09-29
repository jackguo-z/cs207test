from roots import *

def test_L2():
    assert L2([3,4]) == 5.0
    
def test_L2_type():
    try:
        L2(['a','b'])
    except TypeError as err:
        assert(type(err) == TypeError)
        
def test_L2_weighted():
    assert L2([3,4],[1,2]) == 8.5440037453175304
        
def test_L2_length():
    try:
        L2([3,4],[1,2,3])
    except ValueError as err:
        assert(type(err) == ValueError)
