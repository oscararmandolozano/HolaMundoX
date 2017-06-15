#!/usr/bin/python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
class ourwindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Primer Programa")
		Gtk.Window.set_default_size(self, 800,625)
		Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)
		button1 = Gtk.Button("Hola mundo")
		button1.connect("clicked", self.whenbutton1_clicked)
		self.add(button1)
	def whenbutton1_clicked(self, button):
		print "Preionado Hola mundo!"

window = ourwindow()        
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
