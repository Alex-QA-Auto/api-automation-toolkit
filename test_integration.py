import os
import pytest

def test_log_file_exists():
    # Проверяем, что система логирования создала файл
    assert os.path.exists("beast_sense.log") == True

def test_best_coin_saved():
    # Проверяем, что цель была найдена и записана
    assert os.path.exists("best_coin.txt") == True
