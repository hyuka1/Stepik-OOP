from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + " "

    @staticmethod
    def check_card_number(nums):
        nums = nums.split("-")

        if len(nums) == 4 and all(True if i.isdigit() and len(i) == 4 else False for i in nums):
            return True
        else:
            return False

    @classmethod
    def check_name(cls, name):
        if len(name.split()) == 2:
            for x in name:
                if x not in cls.CHARS_FOR_NAME:
                    return False

            else:
                return True
        else:
            return False
