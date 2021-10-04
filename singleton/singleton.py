class Singleton(object):

    _instance = None

    def __new__(self, *args, **kwargs):

        if self._instance is None:

            self._instance = super(Singleton, self).__new__(self)

        return self._instance

sing_1 = Singleton()
sing_2 = Singleton()

print(f"object 1: {sing_1}")
print(f"object 2: {sing_2}")