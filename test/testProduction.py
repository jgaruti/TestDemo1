
import pytest
import ProductionCode
def test_good_list():
    test_data = ["Hi Hi Hi there you%%",
                 "There Hi RTRE$^%$  $#%$#FGF %$^Hi"]
    counts = ProductionCode.count_words(test_data)
    assert "Hi" in counts
    assert counts["Hi"] ==5