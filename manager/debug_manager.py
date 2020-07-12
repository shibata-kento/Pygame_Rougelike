class DebugManager():

    is_debug = True

    __test = 50
    level = __test
    floor = __test
    potion = __test
    bom = __test

    @classmethod
    def print(cls, text: str):
        if not cls.is_debug:
            return
        print(text)