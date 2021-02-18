from pathlib import Path

pythondir = Path(__file__).parent
rootdir = pythondir.parent.resolve()
datadir = rootdir.joinpath('data')