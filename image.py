from urllib import quote
import re
import requests
from random import shuffle

def image(searchterm, unsafe=False):
    searchterm = quote(searchterm)

    # if unsafe else safe = "&safe=active"

    safe = "&safe=" 
    searchurl = "https://www.google.com/search?tbm=isch&q={0}{1}".format(searchterm, safe)

    # this is an old iphone user agent. Seems to make google return good results.
    useragent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Versio  n/4.0.5 Mobile/8A293 Safari/6531.22.7"

    result = requests.get(searchurl, headers={"User-agent": useragent}).text

    images = re.findall(r'imgurl.*?(http.*?)\\', result)
    shuffle(images)

    return images[0] if images else ""
