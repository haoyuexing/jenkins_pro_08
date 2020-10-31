import pytest


class TestLogout:
    @pytest.mark.run(order=3)
    def test_logout4(self):
        print("logout4")

    @pytest.mark.run(order=3)
    def test_logout5(self):
        print("logout4")


    @pytest.mark.run(order=3)
    def test_logout6(self):
        print("logout4")
