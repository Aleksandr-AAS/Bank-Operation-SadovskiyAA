from src.decorators import log


def test_log_console_ok(capsys):
    @log()
    def get_multiplic1(a, b):
        return a / b

    get_multiplic1(10, 2)
    captured = capsys.readouterr()
    assert "Имя функции" in captured.out


def test_log_console_error(capsys):
    @log()
    def get_multiplic1(a, b):
        return a / b

    get_multiplic1(10, 0)
    captured = capsys.readouterr()
    assert "error" in captured.out


def test_log_ok():
    @log("logfile.txt")
    def get_multiplicat(a, b):
        return a / b

    get_multiplicat(10, 4)
    with open("logfile.txt", "r", encoding="utf-8") as file:
        log_content = file.read()

    assert "Имя функции" in log_content


def test_log_error():
    @log("logfile.txt")
    def get_multiplicat(a, b):
        return a / b

    get_multiplicat(10, 0)
    with open("logfile.txt", "r", encoding="utf-8") as file:
        log_content = file.read()

    assert "error" in log_content
