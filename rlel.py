import wx
from MainWindow import MainWindow

if __name__ == "__main__":
	app = wx.App(False)
	
	main_window = MainWindow(None, "Rapid Light EVE Launcher")
	app.MainLoop()