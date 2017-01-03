# -*- coding: utf-8 -*-

# Scrapy settings for zhihu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihu'

SPIDER_MODULES = ['zhihu.spiders']
NEWSPIDER_MODULE = 'zhihu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

IMAGES_STORE = 'D:\\xx'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihu.middlewares.ZhihuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhihu.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'zhihu.pipelines.ZhihuPipeline': 300,
   'scrapy.contrib.pipeline.images.ImagesPipeline': 100,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

ZHIHU_HEADERS = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate, sdch, br',
	'Cache-Control':'no-cache',
	'Host':'www.zhihu.com',
	'Accept-Language':'zh-CN,zh;q=0.8',
	'Referer':'https://www.zhihu.com/',
	'Upgrade-Insecure-Requests':'1',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

ZHIHU_COOKIE = {
	"d_c0":"ACDAxLoxjgqPTordz-EBnQLOkUKgqqv6Xn4=|1474121186",
	" _za":"20dce70c-1d0e-4888-96aa-1bc6a74af21f",
	" _zap":"f83dd296-4b66-4ca1-9c42-9007e5464eb4",
	" _ga":"GA1.2.490362985.1476722369",
	" q_c1":"c92d33dc12274512aa34f5336157668a|1482310399000|1474121186000",
	" l_cap_id":"ODk4OTJhOGFkMjFmNDc5OWEzMWIzMjQyMGM4N2E4OTA=|1483336471|e7a2aa4c4800ffa28d6e87fa5da63f270b124743",
	" cap_id":"ZjY1NzYzMzQzMGM0NDJkNWIzMmQ5OWI2ZDdhNzlmOWU=|1483336471|18908f38f1b91612ddbb483f2d738cecaab63e64",
	" _xsrf":"1e77a54e3790ee4d5babbba73af30f31",
		" __utmt":"1",
	" r_cap_id":"ZmNmYjFiODE1MmZlNDNiYWE5ZjYyOGZiMzZiNmM5MzM=|1483336667|dbe340b6686110aa2650ecf6dbeb85de05cee743",
	" login":"MjA0YjFmNTgxNjc2NGViNThiZTlkZjZmYzJkZTk2NmE=|1483336685|a75c863ed8e41bb5fe88baee86dae4949538ef1f",
	" unlock_ticket":"QUNDQTJkOXRPZ29YQUFBQVlRSlZUVEh6YVZqNjNnQVBFcHpEeURNRHRrTmxsbEFhS2ZORXFRPT0=|1483336745|bccb1f8901366b028f46eefdf297266cc6e420ce",
	" n_c":"1",
	" __utma":"51854390.490362985.1476722369.1482908694.1483336667.2",
	" __utmb":"51854390.4.10.1483336667",
	" __utmc":"51854390",
	" __utmz":"51854390.1483336667.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic",
	" __utmv":"51854390.100--|2=registration_date=20160714=1^3=entry_date=20160714=1",
	" z_c0":"Mi4wQUNDQTJkOXRPZ29BSU1ERXVqR09DaGNBQUFCaEFsVk5LWG1SV0FCZFF5U1N0T0RwWEQ2dFdRSHdzUmxwMHVqUVZR|1483336751|98cb2c3003e0772c8a034cdba49aec98b8cfcd1a",
	
}

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10