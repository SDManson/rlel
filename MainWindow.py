import wx

class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(425,383),
			style=wx.DEFAULT_FRAME_STYLE & ~wx.RESIZE_BORDER)
		self.SetBackgroundColour("white")

		eve_path = wx.TextCtrl(self, wx.ID_ANY,
			 "path to eve install root", pos=wx.Point(12,12), size=wx.Size(220,23))
		singularity_radio = wx.CheckBox(self, wx.ID_ANY, pos=wx.Point(242, 12), label="Singularity")
		eve_path_browse_button = wx.Button(self, wx.ID_ANY, "Browse",
			pos=singularity_radio.Position + wx.Size(singularity_radio.Size.width,0) + wx.Point(12,0),
			size=wx.Size(70,23))
		self.account_box = wx.ListBox(self, wx.ID_ANY, pos=wx.Point(12, 48), size=wx.Size(300,280),
		choices=["character", "select", "goes", "here"],
		style=wx.LB_MULTIPLE)
		self.save_button = wx.Button(self, wx.ID_ANY, "Save", size=wx.Size(88, 23), pos=wx.Point(318,48))
		self.launch_button = wx.Button(self, wx.ID_ANY, "Launch", size=wx.Size(88,23), pos=wx.Point(318,0)+(wx.Point(0,self.save_button.Position.y + self.save_button.Size.height + 2)))
		self.add_char_button = wx.Button(self, wx.ID_ANY, "Add Character", size=wx.Size(88,23),  pos=wx.Point(318,0)+(wx.Point(0,self.launch_button.Position.y + self.launch_button.Size.height + 2)))
		self.remove_char_button = wx.Button(self, wx.ID_ANY, "Remove Char", size=wx.Size(88,23),  pos=wx.Point(318,0)+(wx.Point(0,self.add_char_button.Position.y + self.add_char_button.Size.height + 2)))
		self.SetIcon(wx.Icon('rlel.ico'))
		self.Bind(wx.EVT_BUTTON, self.remove_char, id=self.remove_char_button.GetId())
		self.Show(True)

	def remove_char(self, event):
		i=0
		for entry in self.account_box.GetSelections():
			self.account_box.Delete(entry-i)
			i+=1
		return
	