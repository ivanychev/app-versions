import requests
import xmltodict
import os
import fnmatch
from collections import namedtuple
from operator import itemgetter

Path = namedtuple("Path", ["string", "length"])

def parse_version(url):
    r = requests.get(url)
    rdict = xmltodict.parse(r.text)
    return rdict["rss"]["channel"]["item"]["enclosure"]["@sparkle:version"]

def get_plists(app_path):
    matches = []
    for root, dirnames, filenames in os.walk(app_path):
        for filename in fnmatch.filter(filenames, 'Info.plist'):
            matches.append(os.path.join(root, filename))
    paths = list(filter(lambda s: "Sparkle" not in s, matches))
    paths_lengthed = map(lambda x: Path(x, x.count("/")), paths)
    return sorted(paths_lengthed, key=itemgetter("length"))[0]

get_plists("/Applications/Flux.app")
