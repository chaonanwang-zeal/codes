import pytest
from tester.algo import findRedundantConnection


def test_findRedundantConnection():
    # Test case 1
    edges1 = [[1, 2], [1, 3], [2, 3]]
    assert findRedundantConnection(edges1) == [2, 3]

    # Test case 2
    edges2 = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    assert findRedundantConnection(edges2) == [1, 4]

    # Test case 3
    edges3 = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]
    assert findRedundantConnection(edges3) == [41, 1]


if __name__ == "__main__":
    pytest.main()
