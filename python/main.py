from config import datadir, rootdir

print("\nThe project root is located here:")
print(rootdir)

print("\nThe datadir directory is located here:")
print(datadir)

items = list(datadir.glob('*'))
files = [item for item in items if item.is_file()]
dirs = [item for item in items if item.is_dir()]

if dirs:
    print("\nThe datadir contains these directories:")
    for d in dirs:
        print("-", d.relative_to(datadir))
else:
    print("\nThe datadir does not contain any directory.")

if files:
    print("\nThe datadir contains these files:")
    for f in files:
        print("-", f.relative_to(datadir))
else:
    print("\nThe datadir does not contain any file.")
