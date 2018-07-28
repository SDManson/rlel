import wx
import os

class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(425,383),
			style=wx.DEFAULT_FRAME_STYLE & ~wx.RESIZE_BORDER)
		self.SetBackgroundColour("white")

		self.eve_path = wx.DirPickerCtrl(self, wx.ID_ANY, style=wx.FLP_USE_TEXTCTRL,
			pos=wx.Point(12,12), size=wx.Size(310,23))
		self.eve_path.TextCtrl.Size=wx.Size(240,23)
		self.eve_path.PickerCtrl.Position=wx.Point(240,0)
		self.eve_path.PickerCtrl.Size=wx.Size(70,23)
		self.singularity_radio = wx.CheckBox(self, wx.ID_ANY, pos=wx.Point(324, 15), label="Singularity")
		self.account_box = wx.ListBox(self, wx.ID_ANY, pos=wx.Point(12, 48), size=wx.Size(300,280),
			choices=["character", "select", "goes", "here"],
			style=wx.LB_MULTIPLE)
		self.launch_button = wx.Button(self, wx.ID_ANY, "Launch", size=wx.Size(88,23), pos=wx.Point(318,48))
		self.add_char_button = wx.Button(self, wx.ID_ANY, "Add Character", size=wx.Size(88,23),  pos=wx.Point(318,0)+(wx.Point(0,self.launch_button.Position.y + self.launch_button.Size.height + 2)))
		self.remove_char_button = wx.Button(self, wx.ID_ANY, "Remove Char", size=wx.Size(88,23),  pos=wx.Point(318,0)+(wx.Point(0,self.add_char_button.Position.y + self.add_char_button.Size.height + 2)))
		self.SetIcon(wx.Icon('rlel.ico'))
		self.Bind(wx.EVT_BUTTON, self.remove_char, id=self.remove_char_button.GetId())
		self.eve_path.SetPath(self.get_tranq_path())
		self.SetFocus()
		self.Show(True)

	def remove_char(self, event):
		i=0
		for entry in self.account_box.GetSelections():
			self.account_box.Delete(entry-i)
			i+=1
		return
	
	def get_tranq_path(self):
		path = None
		appdata = os.getenv('LOCALAPPDATA')
		for d in os.listdir(os.path.join(appdata,'ccp','eve')):
			if '_tranquility' in d:
				split = d.split('_')
				if split[-1] == 'tranquility':
					drive = split[0]
					drive = str.capitalize(drive) + ':' + os.sep
					path = os.path.join(drive, *split[1:-1])			
					return path
		return ''


