from xml.sax import make_parser, ContentHandler
from pathlib import Path


class CustomHandler(ContentHandler):
    def __init__(self):
        self.data = []

    def startElement(self, name, attrs):
        attributes = []
        for attr_name, attr_value in attrs.items():
            attributes.append(
                {
                    "name": attr_name,
                    "value": attr_value,
                }
            )
        self.data.append(
            {
                "name": name,
                "attributes": attributes,
            }
        )


def xml_parser(file_path: str) -> list:
    # TODO: comment if not dev
    file_path = Path(__file__).parent.parent.parent / file_path

    parser = make_parser()
    handler = CustomHandler()

    parser.setContentHandler(handler)
    parser.parse(file_path)

    return handler.data
