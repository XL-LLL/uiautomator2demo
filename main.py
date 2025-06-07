import uiautomator2 as u2

"""
#weditor
#usb联接
device = u2.connect("192.168.1.100:5555")
#device(text = '应用名').click()
#device.app_install()
print(device.device_info)
device.press("home")
device(text = '微信').click()
device.swipe(0.5,0.5,0.5,0.9)
device.xpath('//*[@resource-id="com.tencent.mm:id/nz1"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]').click()

"""
#ViewWizard
import pywinauto
from pywinauto.application import Application
from pywinauto  import mouse
#notepad_app = Application(backend="uia").start("notepad.exe")#打开自带的应用
#ViewWizard_app = Application(backend="uia").start("F:\ViewWizard\ViewWizard2.exe")#打开自己安装的应用
#app = Application(backend="uia").connect(process=14260) #进程的联接方式
#app = Application(backend="uia").connect(handle=3343544) #句柄的联接方式
#app = Application(backend="uia").start("F:\WeChat\WeChat.exe")
#app = Application(backend="uia").connect(handle=328296) #句柄的联接方式
#app = Application(backend="uia").start("notepad.exe")#打开自带的应用
#dlg = app["Dialog"]# 通过标题获取窗口
#dlg = app.Dialog# 通过类名获取窗口
#dlg.print_control_identifiers()
#print(dlg.rectangle())#查看坐标
#dialog = dlg['Edit']#选择控件
#dialog.print_control_identifiers()
#dlg = app["Pane"]
#dlg.print_control_identifiers()
#mouse.click(coords=(85,508))
#dlg.click_input()
#dlg = app["Pane"]['Hyperlink6'].type_keys("666")
#dlg = app["Pane"]['Hyperlink6']下一节
#pic = dakai.capture_as_image()
#pic.save("test.jpg")
""" 
app = Application(backend="uia").connect(handle=132360)
yanzgeng = app["Pane"]["Static21"]
paizhao = app["Pane"]['Hyperlink7']


print("开始等待通过")
yanzgeng.wait(wait_for="ready",timeout=1200,retry_interval=1)
print("结束等待通过")
paizhao.click_input()

tupian = app["Pane"]['ListItem8']
tupian.click_input()

dakai = app["Pane"]['打开(O)']
dakai.click_input()
print("操作完成")
ListBox Image3 Static9
"""
app = Application(backend="uia").start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe   " )

dlg = app["backend"]
dlg.print_control_identifiers()

