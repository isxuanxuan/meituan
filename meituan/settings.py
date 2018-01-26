# -*- coding: utf-8 -*-

# Scrapy settings for meituan project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'meituan'

SPIDER_MODULES = ['meituan.spiders']
NEWSPIDER_MODULE = 'meituan.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'meituan (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

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
DEFAULT_REQUEST_HEADERS = {'Accept':'*/*',
'Accept-Encoding':'gzip,deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cookie':'_lxsdk_cuid=161307ff527c8-07a747d26a5206-4323461-144000-161307ff527c8; client-id=51d4d643-a157-4732-ad28-7fa610f1dc18; _lxsdk=16130817dbd94-0753a8d94895d8-4323461-144000-16130817dbec8; mtcdn=K; userTicket=faiBeRLzXaMRQMSKpcksQsAvvCFHOjkZZMEYTxsg; u=133461952; n=MT%E7%8E%84%E7%8E%84; m=xxzspace%40gmail.com; lt=nr6X4FaTNb7RAisa1-OIHZZDhE4AAAAARQUAAHiCBkBGfWoRbtvYqsxjAN51BTORh0-_86dz2JExVFw24w9KQi4HqUbjkHUJz3iBBQ; lsu=xxzspace%40gmail.com; oc=smxI1oqL87_LOT1eh_WyD4bkyNQhdh4uBa7jT5GgZb8_97uBgYmGaXxp_bpvIsMgr5imgELDge7XpNd6tt5P5SeDPoghWE5opKzlRQD6R5c6YXVcADZOndmIDx0C7pV6ghk4qqh97i8OnQOOfhTIQAL1Y5KyPmjrRwyqFBftwpI; token2=nr6X4FaTNb7RAisa1-OIHZZDhE4AAAAARQUAAHiCBkBGfWoRbtvYqsxjAN51BTORh0-_86dz2JExVFw24w9KQi4HqUbjkHUJz3iBBQ; uuid=4ae61de922fe4e48b776.1516937107.2.0.1; em=bnVsbA; om=bnVsbA; unc=MT%E7%8E%84%E7%8E%84; ls=1516937731; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; vipnotice_133461952=%7B%22status%22%3Atrue%2C%22growthValue%22%3A3149%2C%22showLevel%22%3A4%2C%22noticeType%22%3A0%2C%22noticeValue%22%3A0%2C%22cityid%22%3A59%7D; __utma=211559370.350255061.1516939667.1516939667.1516939667.1; __utmc=211559370; __utmz=211559370.1516939667.1.1.utmcsr=blog.csdn.net|utmccn=(referral)|utmcmd=referral|utmcct=/u013243986/article/details/52223438; ci=1; rvct=1%2C59; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; IJSESSIONID=4y93xnjmfxaw14t2eo51koy1o; iuuid=B7F74D0CE1A60228150F28CCC238BB797B49780175FC1693FA6AF80A1758A31C; isid=04EB3BD56B26A244A4D187CC80673F89; oops=nr6X4FaTNb7RAisa1-OIHZZDhE4AAAAARQUAAHiCBkBGfWoRbtvYqsxjAN51BTORh0-_86dz2JExVFw24w9KQi4HqUbjkHUJz3iBBQ; logintype=normal; cityname=%E5%8C%97%E4%BA%AC; lat=39.875941; lng=116.665518; __mta=215374760.1516937148760.1516940480152.1516940775795.22; _lxsdk_s=161307ff528-f3c-894-ec6%7C%7C4',
'Host':'www.meituan.com',
'Proxy-Connection':'keep-alive',
'Referer':'http://www.meituan.com/meishi/1653468/',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'meituan.middlewares.MeituanSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'meituan.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'meituan.pipelines.MeituanPipeline': 300,
#}

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
