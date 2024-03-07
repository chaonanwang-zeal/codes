# tests/test_iss_tracker.py

from iss_tracker import iss_over_head, is_night

def test_iss_over_head():
    # 测试 ISS 是否在头顶附近的情况
    # 在这里，你可以使用 assert 语句来检查函数的返回值是否为 True 或 False
    result = iss_over_head()
    assert result is True or result is False

def test_is_night():
    # 测试是否为晚上的情况
    # 同样，使用 assert 语句检查函数的返回值是否为 True 或 False
    result = is_night()
    assert result is True or result is False
