# -*- coding: utf-8 -*-
import os
import sys
import pyads 
import time 
import glfw
import OpenGL.GL as gl
import imgui
from imgui.integrations.glfw import GlfwRenderer
 
 
 
path_to_font = None # "path/to/font.ttf"
opened_state = True
 
flag_fixed = imgui.WINDOW_NO_MOVE|imgui.WINDOW_NO_COLLAPSE|imgui.WINDOW_NO_RESIZE
offset = 0  #offset y for menu bar
 
def nMFD1(i): #Define global varriable a
    global a
    a = i #initialize global variable a
nMFD1(1)
def nMFD2(i): #Define global varriable a
    global b
    b = i #initialize global variable a
nMFD2(1)
def nMFD3(i): #Define global varriable a
    global c
    c = i #initialize global variable a
nMFD3(1)
#MFDs##############################################################################################
def MFD1():
    imgui.button("Button A")
    imgui.button("Button B")
    imgui.button("Button C")
def MFD2():
    imgui.button("Button D")
    imgui.button("Button E")
    imgui.button("Button F")
def MFD3():
    imgui.button("Button G")
    imgui.button("Button H")
    imgui.button("Button I")
def MFD4():
    imgui.begin_group()
    imgui.button("Button A")
    imgui.button("Button B")
    imgui.end_group()
    imgui.same_line(spacing=50)
    imgui.begin_group()
    imgui.bullet_text("Bullet A")
    imgui.bullet_text("Bullet B")
    imgui.end_group()
def MFD5():
    imgui.begin_group()
    imgui.button("Button A",100,30)
    imgui.button("Button B",100,30)
    imgui.end_group()
    imgui.same_line(spacing=40)
    imgui.begin_group()
    imgui.bullet_text("Bullet A")
    imgui.bullet_text("Bullet B")
    imgui.end_group()    
    imgui.same_line(spacing=10)
    imgui.begin_group()
    imgui.color_button("Button 1", 1, 0, 0, 1, 0, 30, 30)
    imgui.color_button("Button 2", 0, 1, 0, 1, 0, 30, 30)  
    imgui.end_group()                
###################################################################################################
def frame_commands():
    gl.glClearColor(0.1, 0.1, 0.1, 1)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
 
    io = imgui.get_io()
 
    if io.key_ctrl and io.keys_down[glfw.KEY_Q]:
        sys.exit(0)
 
    menu = False    
    if menu == True:
       
        if imgui.begin_main_menu_bar():
            if imgui.begin_menu("File", True):
                clicked_quit, selected_quit = imgui.menu_item("Quit", "Ctrl+Q", False, True)
 
                if clicked_quit:
                    sys.exit(0)
 
                imgui.end_menu()
            imgui.end_main_menu_bar()
 
#Window#########################
#imgui.begin(label(str),closable(bool),flags)
#Parameters:
# label (str) - label of the window.
# closable (bool) - define if window is closable.
# flags - Window flags. See: list of available flags.
#List of all available window flags (click to see documentation):
# imgui.WINDOW_NO_TITLE_BAR
# imgui.WINDOW_NO_RESIZE
# imgui.WINDOW_NO_MOVE
# imgui.WINDOW_NO_SCROLLBAR
# imgui.WINDOW_NO_SCROLL_WITH_MOUSE
# imgui.WINDOW_NO_COLLAPSE
# imgui.WINDOW_ALWAYS_AUTO_RESIZE
# imgui.WINDOW_NO_SAVED_SETTINGS
# imgui.WINDOW_NO_INPUTS
# imgui.WINDOW_MENU_BAR
# imgui.WINDOW_HORIZONTAL_SCROLLING_BAR
# imgui.WINDOW_NO_FOCUS_ON_APPEARING
# imgui.WINDOW_NO_BRING_TO_FRONT_ON_FOCUS
# imgui.WINDOW_ALWAYS_VERTICAL_SCROLLBAR
# imgui.WINDOW_ALWAYS_HORIZONTAL_SCROLLBAR
# imgui.WINDOW_ALWAYS_USE_WINDOW_PADDING
#Returns:
# tuple - (expanded, opened) tuple of bools. If window is collapsed expanded==True.
# The value of opened is always True for non-closable and open windows but changes state
# to False on close button click for closable windows.
 
#############################################
#Window MFD 1################################
    imgui.set_next_window_size(300, 300)
    imgui.set_next_window_position(0, 0+offset)
    imgui.begin("1", flags=flag_fixed|imgui.WINDOW_MENU_BAR|imgui.WINDOW_NO_TITLE_BAR)
    if imgui.begin_menu_bar():
        if imgui.begin_menu('Menu'):
            clicked1, state = imgui.menu_item('MFD1','MFD1')
            if clicked1:
                nMFD1(1)
            clicked2, state = imgui.menu_item('MFD2','MFD2')
            if clicked2:
                nMFD1(2)
            clicked3, state = imgui.menu_item('MFD3','MFD3')
            if clicked3:
                nMFD1(3)
            clicked4, state = imgui.menu_item('MFD4','MFD4')
            if clicked4:
                nMFD1(4)
            clicked5, state = imgui.menu_item('MFD5','MFD5')
            if clicked5:
                nMFD1(5)                                    
            imgui.end_menu()            
        imgui.end_menu_bar()
        if a == 1:
            MFD1()
        if a == 2:
            MFD2()
        if a == 3:
            MFD3()
        if a == 4:
            MFD4()
        if a == 5:
            MFD5()                        
    imgui.end()
#############################################
#Window MFD 2################################
    imgui.set_next_window_size(300, 300)
    imgui.set_next_window_position(300, 0+offset)
    imgui.begin("2", flags=flag_fixed|imgui.WINDOW_MENU_BAR|imgui.WINDOW_NO_TITLE_BAR)
    if imgui.begin_menu_bar():
        if imgui.begin_menu('Menu'):
            clicked1, state = imgui.menu_item('MFD1','MFD1')
            if clicked1:
                nMFD2(1)
            clicked2, state = imgui.menu_item('MFD2','MFD2')
            if clicked2:
                nMFD2(2)
            clicked3, state = imgui.menu_item('MFD3','MFD3')
            if clicked3:
                nMFD2(3)
            clicked4, state = imgui.menu_item('MFD4','MFD4')
            if clicked4:
                nMFD2(4)
            clicked5, state = imgui.menu_item('MFD5','MFD5')
            if clicked5:
                nMFD2(5)                                    
            imgui.end_menu()            
        imgui.end_menu_bar()
        if b == 1:
            MFD1()
        if b == 2:
            MFD2()
        if b == 3:
            MFD3()
        if b == 4:
            MFD4()
        if b == 5:
            MFD5()                        
    imgui.end()
 #############################################
#Window MFD 3################################
    imgui.set_next_window_size(300, 300)
    imgui.set_next_window_position(600, 0+offset)
    imgui.begin("3", flags=flag_fixed|imgui.WINDOW_MENU_BAR|imgui.WINDOW_NO_TITLE_BAR)
    if imgui.begin_menu_bar():
        if imgui.begin_menu('Menu'):
            clicked1, state = imgui.menu_item('MFD1','MFD1')
            if clicked1:
                nMFD3(1)
            clicked2, state = imgui.menu_item('MFD2','MFD2')
            if clicked2:
                nMFD3(2)
            clicked3, state = imgui.menu_item('MFD3','MFD3')
            if clicked3:
                nMFD3(3)
            clicked4, state = imgui.menu_item('MFD4','MFD4')
            if clicked4:
                nMFD3(4)
            clicked5, state = imgui.menu_item('MFD5','MFD5')
            if clicked5:
                nMFD3(5)                                    
            imgui.end_menu()            
        imgui.end_menu_bar()
        if c == 1:
            MFD1()
        if c == 2:
            MFD2()
        if c == 3:
            MFD3()
        if c == 4:
            MFD4()
        if c == 5:
            MFD5()                        
    imgui.end()  
###################################################################################################
def render_frame(impl, window, font):
    glfw.poll_events()
    impl.process_inputs()
    imgui.new_frame()
 
    gl.glClearColor(0.1, 0.1, 0.1, 1)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
 
    if font is not None:
        imgui.push_font(font)
    frame_commands()
    if font is not None:
        imgui.pop_font()
 
    imgui.render()
    impl.render(imgui.get_draw_data())
    glfw.swap_buffers(window)
 
 
def impl_glfw_init():
    width, height = 900, 900
    window_name = "minimal ImGui/GLFW3 example"
 
    if not glfw.init():
        print("Could not initialize OpenGL context")
        sys.exit(1)
 
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)
 
    window = glfw.create_window(int(width), int(height), window_name, None, None)
    glfw.make_context_current(window)
 
    if not window:
        glfw.terminate()
        print("Could not initialize Window")
        sys.exit(1)
 
    return window
 
 
def main():
    imgui.create_context()
    window = impl_glfw_init()
 
    impl = GlfwRenderer(window)
 
    io = imgui.get_io()
    jb = io.fonts.add_font_from_file_ttf(path_to_font, 30) if path_to_font is not None else None
    impl.refresh_font_texture()
 
    while not glfw.window_should_close(window):
        render_frame(impl, window, jb)
 
    impl.shutdown()
    glfw.terminate()
def ads():
    plc = pyads.Connection('5.97.120.151.1.1', pyads.PORT_TC3PLC1)
    try:
        plc.open()
    except:
        print("Connection Failed")
    else:
        print("Connected")

        while True:
            # read int value by name
            #i = plc.read_by_name("PRG_SystemTime.sTimeStamp")
            #print(i)
            # write int value by name
            #plc.write_by_name("GVL.int_val", i)
            time.sleep(1)
        # close connection
    plc.close()     
 
if __name__ == "__main__":
    main()
