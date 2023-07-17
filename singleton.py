class Singleton:
    _instance = None

    def __new__(cls):
        if cls.instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance