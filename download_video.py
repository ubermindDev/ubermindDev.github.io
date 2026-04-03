import urllib.request
import re

urls = [
    'https://pixabay.com/videos/forest-path-trees-nature-woods-14138/',
    'https://pixabay.com/videos/trail-running-runner-forest-path-13174/'
]

for url in urls:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        # look for mp4 link
        links = re.findall(r'https://cdn\.pixabay\.com/video/[^\"' + "'" + r']+\.mp4', html)
        if links:
            print('Found link:', links[0])
            urllib.request.urlretrieve(links[0], 'C:/goodMyself/my-blog/static/bg-trail.mp4')
            print('Downloaded!')
            break
        else:
            print('No links found for', url)
    except Exception as e:
        print('Error:', e)
