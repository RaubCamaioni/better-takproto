## better-takproto

[Betterproto](https://pypi.org/project/betterproto/) creates pythonic protobuf bindings.
Utalizing the protobuf definitions from [takproto](https://github.com/snstac/takproto/tree/main)
Read the Betterproto documentation for all the advantages over the Google implimentation.

## rebuilding protobug python binding

Install dependencies
```
pip install betterproto[compiler]
```

Rebuild python bindings
```
python -m grpc_tools.protoc -I . --python_betterproto_out=./src/takproto ./proto/tak.proto
```

Recompile generates am empty __init__.py
Add the following for usage convenience.
```
__version__ = "<version>"
from takproto.takproto import *
``