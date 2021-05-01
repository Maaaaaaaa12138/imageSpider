### scrapy壁纸爬虫

**写在开头**

[壁纸网站](http://www.bizhi88.com/)

**用法**

直接克隆使用:

```
git clone https://github.com/Maaaaaaaa12138/imageSpider.git
cd imageSpider
pip install -r requirements.txt
scrapy crawl imageSp1
```

运行完毕后爬取的图片存于imgs下

**自定义**

- 爬取该网站的其他类别：修改`spiders/spider.py`中第十行url中域名后面的`c1`, 已知类别:
    - c1 : 美女壁纸
    - c2 : 风景壁纸
    - c3 : 动漫壁纸
    - c4 : 动物壁纸
    - 更多类别请去[源网站](http://www.bizhi88.com/)->分类下寻找

- 爬取其他壁纸网站请自行修改`spiders/spider.py`文件
