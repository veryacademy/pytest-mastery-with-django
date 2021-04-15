# #https://docs.pytest.org/en/reorganize-docs/new-docs/user/assert_statements.html
# # Assertions are the condition or boolean expression which are always supposed to be true
# import pytest

# def vowels():
#     return set('aeiou')

# @pytest.mark.skip
# def test_vowels():
#     result =  vowels()
#     expected = set('aeiou')
#     print ("this test has run")
#     assert result == expected