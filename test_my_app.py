import pytest
from IPython.external.qt_for_kernel import QtCore
from _pytest import tmpdir

import my_logger
import main_window
import alg_luhn, graph, read_settings, gen_num, write_result


# @pytest.fixture
# def app(qtbot) -> main_window.Window:
#
#     my_app = main_window.Window()
#     qtbot.addWidget(my_app)
#     return my_app
#
#
# def test_start(app):
#     app.variant_label = '5'
#     assert app.variant_label.text() == '5'
#
#
# def test_start_label(app, qtbot):
#     app.variant_label.setText("5")
#     qtbot.mouseClick(app.button_start, QtCore.Qt.LeftButton)
#     assert app.text_label.text() == "5"


@pytest.mark.xfail()
@pytest.mark.parametrize("numbers", ['4529618049607621', '4538912735659316', '8225904637281519', '6352219737721156',
                                     '3872278836666320', '6094581715564255', '5166045463141790',
                                     '1498845182739705', '3206572148911478', '2202202138745688', '7638294589620560'])
def test_luhn(numbers):
    """Тест провален если последовательность не прошла проверку"""

    assert alg_luhn.alg_luhn(numbers)


def test_graph():
    """Тест провалится если два массима разной длины"""

    cores = [7, 14, 11, 8, 15, 3, 6, 2, 13, 1, 9, 4, 5, 10, 12]
    times = [13, 10, 7, 9, 5, 2, 11, 6, 14, 4, 1, 3, 12, 8, 5]
    assert graph.show_plt(cores, times)


@pytest.mark.xfail()
def test_read_settings():
    """я ожидаю что на самом деле ошибок нет, а значит при таком раскладе тест провален.."""

    with pytest.raises((KeyError, FileNotFoundError)):
        read_settings.read_json("20")


def test_write_file(tmpdir):
    text = "Вечер смешных шуток" \
           "– Почему птицы летят на юг? " \
           "– Потому что они не дойдут."

    a_sub_dir = tmpdir.mkdir('folder')
    a_file = a_sub_dir.join("text.txt")
    write_result.write_file(a_file, text)
    assert text == a_file.read()



