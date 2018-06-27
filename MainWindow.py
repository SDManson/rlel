import wx

class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(425,383))
		self.SetBackgroundColour("white")

		eve_path = wx.TextCtrl(self, wx.ID_ANY,
			 "path to eve install root", pos=wx.Point(12,12), size=wx.Size(220,23))
		singularity_radio = wx.RadioButton(self, wx.ID_ANY, pos=wx.Point(242, 12), label="Singularity")
		singularity_radio.Bind(wx.EVT_LEFT_DOWN, self.singularity_click)
		eve_path_browse_button = wx.Button(self, wx.ID_ANY, "Browse",
			pos=singularity_radio.Position + wx.Size(singularity_radio.Size.width,0) + wx.Point(12,0),
			size=wx.Size(70,23))
		account_box = wx.ListBox(self, wx.ID_ANY, pos=wx.Point(12, 48), size=wx.Size(300,280),
		choices=["character", "select", "goes", "here"])
		save_button = wx.Button(self, wx.ID_ANY, "Save", size=wx.Size(88, 23), pos=wx.Point(318,48))
		launch_button = wx.Button(self, wx.ID_ANY, "Launch", size=wx.Size(88,23), pos=wx.Point(318,0)+(wx.Point(0,save_button.Position.y + save_button.Size.height + 2)))
		add_char_button = wx.Button(self, wx.ID_ANY, "Add Character", size=wx.Size(88,23),  pos=wx.Point(318,0)+(wx.Point(0,launch_button.Position.y + launch_button.Size.height + 2)))
		remove_char_button = wx.Button(self, wx.ID_ANY, "Remove Char", size=wx.Size(88,23),  pos=wx.Point(318,0)+(wx.Point(0,add_char_button.Position.y + add_char_button.Size.height + 2)))
		self.SetIcon(wx.Icon('rlel.ico'))
		self.Show(True)

	def singularity_click(self, event):
		event.GetEventObject().SetValue(not event.GetEventObject().GetValue())