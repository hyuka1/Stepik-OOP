from string import ascii_lowercase, digits


# здесь объявляйте классы TextInput и PasswordInput
class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    @classmethod
    def check_name(cls, name):
        if 3 <= len(name) <= 50 and (False not in (False if x not in cls.CHARS_CORRECT else True for x in name)):
            return name
        else:
            raise ValueError("некорректное поле name")

    def __init__(self, name, size=10):
        self.name = name
        self.size = size
        self.check_name(self.name)

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"


class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    @classmethod
    def check_name(cls, name):
        if 3 <= len(name) <= 50 and (False not in (False if x not in cls.CHARS_CORRECT else True for x in name)):
            return name
        else:
            raise ValueError("некорректное поле name")

    def __init__(self, name, size=10):
        self.name = name
        self.size = size
        self.check_name(self.name)

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
