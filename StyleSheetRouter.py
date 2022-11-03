class StyleSheetRouter:
    def __init__(self, routing_object, basic_key="", basic_filepath=""):
        self.routing_object = routing_object
        self.stylesheets = {}
        if basic_key and basic_filepath:
            self.__setitem__(key=basic_key, filepath=basic_filepath)

    def __setitem__(self, key, filepath):
        with open(filepath, "r") as f:
            self.stylesheets[key] = f.read()
        self.__update()

    def __delitem__(self, key):
        self.stylesheets.pop(key)
        self.__update()

    def __getitem__(self, key):
        return self.stylesheets[key]

    def __update(self):
        styles = "\n".join(self.stylesheets.values())
        self.routing_object.setStyleSheet(styles)

    def add(self, key, filepath: str):
        self.__setitem__(key=key, filepath=filepath)

    def get(self, key):
        self.__getitem__(key=key)

    def remove(self, key):
        self.__delitem__(key=key)

    def get_styles(self):
        return "\n".join(self.stylesheets.values())

    def keys(self):
        return self.stylesheets.keys()
