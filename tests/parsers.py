from html.parser import HTMLParser


class AnchorSearchParser(HTMLParser):
    found = False

    def __init__(self, path):
        super().__init__()
        self.path = path

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if (
            tag.lower() == "a"
            and "href" in attrs
            and self.path == attrs["href"]
        ):
            self.found = True


class PostFormParser(HTMLParser):
    found = False

    def __init__(self):
        super().__init__()
        self.inputs = {}
        self.selects = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if (
            tag.lower() == "form"
            and "method" in attrs
            and "post" == attrs["method"].lower()
        ):
            self.found = True
        elif tag.lower() == "input":
            self.inputs[attrs["name"]] = attrs
        elif tag.lower() == "select":
            self.selects[attrs["name"]] = attrs
