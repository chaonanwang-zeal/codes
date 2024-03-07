from tracker import iss_over_head, is_night

def test_iss_over_head():
    result = iss_over_head()
    assert result is True or result is False

def test_is_night():
    result = is_night()
    assert result is True or result is False
