import os, ast

class Cache:

    def check_cache():
        if os.path.isfile("./nws/locator/cache.txt") == True:
            return True
        else:
            return False

    def read_cache():
        with open("./nws/locator/cache.txt", mode='r') as cache_file:
            cached_coords = cache_file.read()
            # must be converted back to dict if office_lookup will work
            try:
                dict_coords = ast.literal_eval(cached_coords)
            except SyntaxError:
                raise ValueError('ERROR: cache.txt cannot be empty. Please delete file and try again.')
        return dict_coords

    def write_cache(coordinates):
        cache_file = open("./nws/locator/cache.txt", mode='w')
        cache_file.write(str(coordinates))

    def delete_cache():
        os.remove("./nws/locator/cache.txt")
