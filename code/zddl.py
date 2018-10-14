# coding=gbk
from selenium import webdriver
from PIL import Image, ImageEnhance
import pytesseract
import os,time
import PIL.ImageOps

chromedriver = "D:\chromedriver.exe"  # 这里写本地的chromedriver 的所在路径
os.environ["webdriver.Chrome.driver"] = chromedriver  # 调用chrome浏览器
# 加启动配置,启动浏览器不再出现"Chrome正在受到自动软件的控制""
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
driver = webdriver.Chrome(chromedriver, chrome_options=option)
#driver.get("http://221.192.190.15:7001/")  # 该处为具体网址
driver.get("http://121.28.169.98:8080/admin/")  # 该处为具体网址
driver.refresh() #刷新页面
driver.maximize_window()   # 浏览器最大化
# 获取全屏图片，并截取验证码图片的位置
driver.save_screenshot('a.png')
location = driver.find_element_by_id('imgCode').location
size = driver.find_element_by_id('imgCode').size
left = location['x']
top = location['y']
right = location['x']  + size['width']
bottom = location['y']  + size['height']
print(left,right)
a = Image.open("a.png")
im = a.crop((left,top,right,bottom))
im.save("b.png")
time.sleep(1)

# 打开保存的验证码图片
image = Image.open("b.png")
# 图片转换成字符
# sharp_img = image.convert('L')
# sharp_img = ImageEnhance.Contrast(sharp_img).enhance(4.0)
# sharp_img.save("b.png")
# sharp_img.load()  # 对比度增强
# #sharp_img =Image.open("b.png")
# sharp_img = sharp_img.resize((120,38))
# print(sharp_img)
# time.sleep(2)
# vcode = pytesseract.image_to_string(sharp_img,"eng")

def initTable(threshold=140):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table


# 图片的处理过程
im = image.convert('L')
binaryImage = im.point(initTable(), '1')
im1 = binaryImage.convert('L')
im2 = PIL.ImageOps.invert(im1)
im3 = im2.convert('1')
im4 = im3.convert('L')

# 将图片字符放大
out = im1.resize((120,38))
time.sleep(1)
vcode = pytesseract.image_to_string(out)
out.save('3.png')
print("lll:", vcode)


# 填充用户名 密码 验证码
#driver.find_element_by_name("login").send_keys("gccl_liucuifen")
driver.find_element_by_name("userName").send_keys("sjz")
driver.find_element_by_name("password").send_keys("sjz1234")
#driver.find_element_by_name("passwd").send_keys("aaa111!!")
driver.find_element_by_name("code").send_keys(vcode)
# 点击登录
#elem_pwd = driver.find_element_by_name("password")
#elem_pwd.send_keys(Keys.RETURN)

driver.find_element_by_class_name("button").click()