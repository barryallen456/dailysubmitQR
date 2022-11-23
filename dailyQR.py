from time import sleep
import pyautogui
from PIL import ImageGrab, Image
from wxauto import WeChat
import os

number=1
def left_click(img):
	global number
	wechaticon = Image.open(img)
	# 截图当前屏幕并找到之前加载的按钮截图
	msg = pyautogui.locateOnScreen(wechaticon, grayscale=True, confidence=.9)
	if msg == None:
		print("sorry, no found!")
		if img == "wechat.png":
			left_click("showhideicon.png")
			sleep(0.5)
			left_click("wechat2.png")
			sleep(0.5)

	else:

		x, y, width, height = msg
		print("第{}图标在屏幕中的位置是：X={},Y={}，宽{}像素,高{}像素".format(number,x, y, width, height))

		# 左键点击屏幕上的这个位置
		pyautogui.FAILSAFE = False
		pyautogui.click(x+18, y+18, button='left')
	number= number + 1
#事先对按钮截图
sleep(1)

left_click("wechat.png")
sleep(0.5)

left_click("search.png")
sleep(0.5)

left_click("yueshengshi.png")
sleep(8)

left_click("yuekangma.png")
sleep(0.5)

left_click("mini.png")
sleep(3)

# target = pyautogui.screenshot(region=[720,20,475,1000])
target = pyautogui.screenshot(region=[0,0,1920,1080])
target.save('target.png')
print("截图保存成功")

left_click("exit.png")
sleep(0.5)

left_click("wechat.png")
sleep(0.5)

wx=WeChat()
wx.GetSessionList()
wx.ChatWith("我是人名")
wx.SendFiles(os.getcwd()+"/target.png")
