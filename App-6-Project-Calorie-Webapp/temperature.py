from selectorlib import Extractor
import requests

class Temperature:
    """
    A scrapper that uses an yml file to read the xpath of a value it needs to extract
    from the timeanddate.com/weather/ url
    """

    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.9',
    }
    base_url = 'https://www.timeanddate.com/weather/'
    yml_path = 'temperature.yaml'

    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def _build_url(self):
       """Builds the url string adding country and city"""
       url = self.base_url + self.country + "/" + self.city
       return url

    def _scrape(self):
       """Extracts a value as instructed by the yml file and returns a dictionary"""
       url = self._build_url()
       extractor = Extractor.from_yaml_file(self.yml_path)
       r = requests.get(url, headers=self.headers)
       full_content = r.text
       raw_content = extractor.extract(full_content)
       return raw_content

    def get(self):
        """Cleans the output of _scrape"""

        scraped_content = self._scrape()
        return float(scraped_content['temp'].replace("°C", "").strip())

if __name__ == "__main__":
    temperature = Temperature("finland", "turku")
    print(temperature.get())