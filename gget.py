import gi
import requests

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Handler:
  def onDestroy(self, *args):
    Gtk.main_quit()
    
  def onButtonPressed(self, button):
    try:
      url = [a.get_text() for a in button.get_parent().get_children() if a.get_name() == 'txtUrl'][0]
      response_box = [b for b in [a for a in button.get_parent().get_children() if a.get_name() == 'scrolledWindow'][0].get_children() if b.get_name() == 'txtResponseView'][0]
      resp = requests.get(url)
      buff = Gtk.TextBuffer()
      buff.set_text(resp.text)
      response_box.set_buffer(buff)
    
    except Exception as e:
      print(e)


builder = Gtk.Builder()
builder.add_from_file("gget.glade")
builder.connect_signals(Handler())

window = builder.get_object("win1")
window.show_all()

Gtk.main()

