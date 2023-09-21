import base64

from IPython.display import Image, display
import matplotlib.pyplot as plt
import shutil
from PIL import Image as PILImage
import requests


def mm(graph):
    graphbytes = graph.encode("ascii")
    base64_bytes = base64.b64encode(graphbytes)
    base64_string = base64_bytes.decode("ascii")
    destination_path = 'class_diagram.jpg'
    image_url = "https://mermaid.ink/img/" + base64_string
    response = requests.get(image_url)
    image_content = response.content
    with open(destination_path, 'wb') as f:
        f.write(image_content)
    display(Image(url="https://mermaid.ink/img/" + base64_string))

mm(
    '''
    classDiagram
    class Animal {
        - name: str
        - age: int
        + make_sound(): str
        + do_trick(): str
    }

    class Lion {
        + make_sound(): str
        + do_trick(): str
    }

    class Dog {
        + make_sound(): str
        + do_trick(): str
    }

    class Elephant {
        + make_sound(): str
        + do_trick(): str
    }

    Animal <|-- Lion
    Animal <|-- Dog
    Animal <|-- Elephant

    '''
)