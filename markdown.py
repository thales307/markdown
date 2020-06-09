import re

def parse(markdown):
    res = markdown
    
    res = re.sub(r'__(.*)__', r'<strong>\1</strong>', res)
    res = re.sub(r'_(.*)_', r'<em>\1</em>', res)
    res = re.sub(r'^\* (.*)', r'<li>\1</li>', res, flags=re.M)
    for i in range(1, 7):
        res = re.sub(r'^{} (.*?$)'.format('#' * i), r'<h{0}>\1</h{0}>'.format(i), res, flags=re.M)
    res = re.sub(r'(\n?<li>.*</li>)', r'<ul>\1</ul>', res, flags=re.S)
    res = re.sub(r'^(?!<[hlu])(.*?$)', r'<p>\1</p>', res, flags=re.M)
    res = re.sub(r'\n', '', res)

    return res