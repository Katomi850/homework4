def check_age(age):
    try:
        assert age >= 18, "Вам має бути 18 років або більше"
        return "Ви можете використовувати цей сервіс"
    except AssertionError as e:
        return str(e)
