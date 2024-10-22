import urllib
import re
import random
import logging

log = logging.getLogger(__name__)


def main(trans, webhook, params):
    error = ''
    comic_src = ''

    try:
        # Third-party dependencies
        try:
            from bs4 import BeautifulSoup
        except ImportError as e:
            log.exception(e)
            return {'success': False, 'error': str(e)}

        # Get latest id
        if 'latest_id' not in webhook.config.keys():
            url = 'https://phdcomics.com/gradfeed.php'
            content = urllib.urlopen(url).read()
            soap = BeautifulSoup(content, 'html.parser')
            pattern = '(?:https://www\.phdcomics\.com/comics\.php\?f=)(\d+)'
            webhook.config['latest_id'] = max([
                int(re.search(pattern, link.text).group(1))
                for link in soap.find_all('link', text=re.compile(pattern))
            ])

        random_id = random.randint(1, webhook.config['latest_id'])
        url = 'https://www.phdcomics.com/comics/archive.php?comicid=%d' % \
            random_id
        content = urllib.urlopen(url).read()
        soup = BeautifulSoup(content, 'html.parser')
        comic_img = soup.find_all('img', id='comic2')

        try:
            comic_src = comic_img[0].attrs.get('src')
        except IndexError:
            pattern = '<img id=comic2 name=comic2 src=([\w:\/\.]+)'
            comic_src = re.search(pattern, content).group(1)

    except Exception as e:
        error = str(e)

    return {'success': not error, 'error': error, 'src': comic_src}
