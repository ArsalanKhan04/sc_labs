import pytest
from GeneratePermutations import gen_perms


# Test 1: Check Permutation size is correct
def test_perm_size():
    assert len(gen_perms("aaaaa", False)) == 120
    assert len(gen_perms("abc", False)) == 6
    assert len(gen_perms("abcd", False)) == 24
    assert len(gen_perms("abcde", False)) == 120
    assert len(gen_perms("aabb", True)) == 6
    assert len(gen_perms("abc", True)) == 6

# Test 2: Check for results
def test_unique_perm_results():
    values = {
        "abc": ["abc", "acb", "bac", "bca", "cab", "cba"],
        "abcd": ["abcd", "abdc", "acbd", "acdb", "adbc", "adcb", "bacd", "badc", "bcad", "bcda", "bdac", "bdca", "cabd", "cadb", "cbad", "cbda", "cdab", "cdba", "dabc", "dacb", "dbac", "dbca", "dcab", "dcba"],
        }
    for key in values:
        assert set(gen_perms(key, False)) == set(values[key])
        assert set(gen_perms(key, False)) == set(values[key])


