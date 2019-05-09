import re
from w import s
import os

# s = 'qweqwe"../../static/icos/guess-u-like.png"eeee'
host = "https://request-wx.xiaoyaz.xyz:8080"


def replace(data):
    def repl(s):
        l, r = s.span()
        # position = dir(s)
        # print(position)
        f = s.string[l:r].find("static") + 6
        result = s.string[l + f:r]
        # print(len(result))
        return '"{}/static{}'.format(host, result)

    result = re.sub(r'"\.\./\.\./static/(.*)?', repl, data)
    print(result)
    return result


for root, dirs, names in os.walk("asd/"):
    for name in names:
        path = root + "/" + name
        print(path)
        if name.endswith(".js") or name.endswith(".json") or name.endswith(".wxml"):
            with open(path, 'r') as f:
                d = f.read()
                d = replace(d)
                # print(d)

            with open(path, "w") as f:
                f.write(d)

replace(s)


# for i in filenames:
#     with open("jesus.js", "w") as file:
#         print(result, file=file)
