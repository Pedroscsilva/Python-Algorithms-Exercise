import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message("stringtest", 2) == "tsetgnir_ts"
    assert encrypt_message("stringtest", 3) == "rts_tsetgni"
    assert encrypt_message("stringtest", 0) == "tsetgnirts"
    with pytest.raises(TypeError):
        encrypt_message(123, 1)
        encrypt_message("stringtest", "stringtest")
