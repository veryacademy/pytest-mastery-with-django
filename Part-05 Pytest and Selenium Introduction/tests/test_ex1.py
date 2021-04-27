# import pytest

# # function  Run once per test
# # class	    Run once per class of tests
# # module	  Run once per module
# # session	  Run once per session

# @pytest.fixture(scope="session")
# def fixture_1():
#    print('run-fixture-1')
#    return 1

# def test_example1(fixture_1):
#     print('run-example-1')
#     num = fixture_1
#     assert num == 1

# def test_example2(fixture_1):
#     print('run-example-2')
#     num = fixture_1
#     assert num == 1