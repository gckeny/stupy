1. 斜体和粗体代码：   
*斜**体* 或 _斜体_    
**粗体**  
***加粗斜体***   
~~删除线~~   
  **加粗**  
2. 标题  
   # 一级标题
   ## 二级标题
   ### 三级标题
   #### 四级标题
   ##### 五级标题
   ###### 六级标题
3. 超链接
欢迎来到[梵居闹市](http://blog.leanote.com/freewalk)  
欢迎来到[梵居闹市](http://blog.leanote.com/freewalk "梵居闹市")  
我经常去的几个网站[Google][1]、[Leanote][2]以及[自己的博客][3][Leanote 笔记][2]是一个不错的[网站][]。  
[1]:http://www.google.com "Google"  
[2]:http://www.leanote.com "Leanote"  
[3]:http://http://blog.leanote.com/freewalk "梵居闹市"  
[网站]:http://http://blog.leanote.com/freewalk
4. 分割线  
   ***
   ---
5. 锚点  
       0. 目录{#index}
      跳转到[目录](#index)  
6. 表格  
|学号 |姓名|分数|  
|---|---|---|  
|小明|男|75|  
|小红|女|79|  
|小陆|男|92|  
7. 代码  
  ```
    #include <stdio.h>
   int main(void)
{
    printf("Hello world\n");
}   
```
8. 引用
   > 第一行  
   > 第二行   
   >>> 多次引用  
   很多次  
   很多很多

9.笔记  
  升级pip: python -m pip install --upgrade pip  
  安装xlrd库: pip install xlrd     
10. 图片添加  
![图片alt](图片地址 ''图片title'')

图片alt就是显示在图片下面的文字，相当于对图片内容的解释。
图片title是图片的标题，当鼠标移到图片上时显示的内容。title可加可不加
![blockchain](https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/
u=702257389,1274025419&fm=27&gp=0.jpg "区块链")


三. 安装三大浏览器驱动driver

???? 1.chromedriver 下载地址：https://code.google.com/p/chromedriver/downloads/list

???? 2.Firefox的驱动geckodriver 下载地址：https://github.com/mozilla/geckodriver/releases/

???? 3.IE的驱动IEdriver 下载地址：http://www.nuget.org/packages/Selenium.WebDriver.IEDriver/



注意：下载解压后，将chromedriver.exe , geckodriver.exe , Iedriver.exe发到Python的安装目录，例如 D:\python 。 然后再将Python的安装目录添加到系统环境变量的Path下面。

然后打开Python IDLE分别输入以下代码来启动不同的浏览器



启动谷歌浏览器

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')



启动火狐浏览器
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://www.baidu.com/')


启动IE浏览器
from selenium import webdriver

browser = webdriver.Ie()
browser.get('http://www.baidu.com/')
--------------------- 
