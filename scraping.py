from lxml import html
import requests

def loaned_amount(lid):
    page = requests.get("https://bitlendingclub.com/user/index/id/"+str(lid))
    tree = html.fromstring(page.text)
    return float(list(tree.xpath('//span[@class="profile-summary-label"]/following-sibling::text()'))[3].split(" ")[1])
