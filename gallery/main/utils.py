import os


def make_tree(path):
    if path:
        media_position = path.index("/media")
        tree = dict(name=os.path.basename(path), children=[], path=path[media_position:])
    try:
        lst = os.listdir(path)
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree['children'].append(make_tree(fn))
            else:
                tree['children'].append(dict(name=name, path=path[media_position:]+"/"+name))
    except OSError:
        pass
    return tree
