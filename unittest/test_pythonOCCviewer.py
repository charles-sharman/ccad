import ccad
import OCC.Display.SimpleGui as SimpleGui

s1 = ccad.sphere(1.0)
display, start_display, add_menu, add_function_to_menu = SimpleGui.init_display()
display.DisplayShape(s1.shape, update=True)
start_display()
