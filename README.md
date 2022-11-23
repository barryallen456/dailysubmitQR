自动截图粤康码并提交
本人测试环境:
    python 3.9
    win10黑色主题(白色主题的朋友们如果不行,可以自己重新截图一下图标)Wechat.png是如果你已经打开会话,在屏幕下面截图的图标,wechar2.png是隐藏在任务栏里的微信图标)两者前提都要打开微信,还有不能多开,微信只能有一个聊天窗口,打开浏览器什么的会失效
    截图区域自己划分,因为pyqt我截图不到
    全屏截图根据自己的屏幕分辨率,在设置->系统->显示里查看
    1920*1080的可以参考这个截图范围根据实际调整)
    # target = pyautogui.screenshot(region=[720,20,475,1000])
    注意在这段中填入群聊或者人的名字
    wx.ChatWith("我是人名")
 
使用方法:
  1.解压并进入文件夹
  2.安装项目依赖
    pip install -r requirement.txt
  3.使用命令
    python dailyQR.py(使用前先把当前文件夹给隐藏了,不然会点文件夹的图标)
    
 效果:
   将截图发到你想发的会话,其他提交方式可自己根据源码去修改
 最后代码写的垃圾能用就好了

问题:安装requirements.txt如果报错请尝试
pip install opencv-python
pip install pywin32
pip install wxauto
pip install pyautogui
