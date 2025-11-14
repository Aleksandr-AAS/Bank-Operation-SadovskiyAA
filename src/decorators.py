from datetime import datetime


def log(filename=None):
    """Декоратор, логирование работы функции"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            if filename is None:
                try:
                    start_date = datetime.now()
                    result = func(*args, **kwargs)
                    print(
                        f"Имя функции {func.__name__} ok, Дата, время вызова функции {start_date},Результат {result}"
                    )
                    return result
                except Exception as error:
                    print(
                        f"Имя функции {func.__name__} error:  {type(error).__name__}.Inputs:{args},{kwargs} "
                        f"Дата, время вызова функции {start_date}"
                    )
                    return "ERROR"
            else:
                try:
                    start_date = datetime.now()
                    result = func(*args, **kwargs)
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(
                            f"Имя функции {func.__name__} ok, Дата, время вызова функции {start_date},"
                            f"Результат {result}\n"
                        )
                        return result
                except Exception as error:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(
                            f"Имя функции {func.__name__} error:  {type(error).__name__}.Inputs:{args},{kwargs} "
                            f"Дата, время вызова функции {start_date}\n"
                        )
                        return "ERROR"

        return wrapper

    return decorator
