from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from colorama import Back, Style 

#Opening Page
Builder.load_string("""
<Homepage>:
    id: Homepage
    name: "Homepage"
    
    GridLayout:
        cols: 1
        
        Button:
            background_normal: "KSquared_Logo.png"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "Tap anywhere to continue"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 100
            text: "KSquared-Mathematics"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 100
            text: "PEMDAS Calculator"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
        
        
                
""")

# Menu
Builder.load_string("""
<Menu>
    id:Menu
    name:"Menu"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Menu"
            
            Button:
                text: "PEMDAS"   
                font_size: '20sp'
                background_color: 0, 0 , 1 , 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "PEMDAS"
                    root.manager.transition.direction = "left" 
                    
            Button:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Visit KSquared-Mathematics"
                on_release:
                    import webbrowser
                    webbrowser.open('https://www.ksquaredmathematics.com/subscribe') 
            
            Button:
                font_size: '20sp'
                background_color: 1, 0, 1, 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "What's new?"
                on_release:
                    app.root.current = "updates"
                    root.manager.transition.direction = "left"
                    
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Share KSquared-Mathematics"
                    
            Image:
                source: 'KSquared_QR.png'
                size_hint_y: None
                height: 800
                width: 800
""")

#Updates
Builder.load_string("""
<updates>
    id:updates
    name:"updates"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
    
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "What's new at KSquared-Mathematics?"
            
            Button:
                id: steps
                text: "Menu"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 0 , 1 , 1
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Menu"
                    root.manager.transition.direction = "right" 
                    
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "PEMDAS Calculator v0.1"
                
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "No new updates as of 1/26/2022"
            
""")

#PEMDAS
Builder.load_string("""
<PEMDAS>
    id:PEMDAS
    name:"PEMDAS"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "PEMDAS"
                
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
            
                Button:
                    id: steps
                    text: "Menu"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        entry.text = ""
                        list_of_steps.clear_widgets() 
            
            TextInput:
                id: entry
                text: entry.text
                hint_text: "Enter expression:"
                multiline: False
                font_size: '35sp'
                size_hint_y: None
                height: 200
                padding: 10
            
            Button:
                id: steps
                text: "Calculate"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets() 
                    PEMDAS.steps(entry.text)    
                       
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

class PEMDAS(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(PEMDAS, self).__init__(**kwargs)
                
    layouts = []
    def steps(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        print("entry",entry)
        
        
        try:
            #Parentheses
            a = entry
            a = a.strip()
            a = a.replace(" ","").replace("??","/").replace("??","*")
            print(a)
            print()
            print("------------------------------")
            print()
            
            a = a.replace(" ","")
            a = a.replace("+-","-")
            a = a.replace("-+","-")
            a = a.replace("+"," + ")
            a = a.replace("-"," - ")
            a = a.replace("**", "^")
            a = a.replace("*"," * ")
            a = a.replace("/"," / ")
            a = a.replace(" ^ - ","^-")
            a = a.replace("^*","^")
            a = a.replace("*(","(")
            a = a.replace("* (","(")
            a = a.replace("(","*(")
            a = a.replace("+ *(","+ (")
            a = a.replace("- *(","- (")
            a = a.replace("^*","^")
            a = a.replace("/ *","/")
            
            
            if a[0] == "*":
                a = a[1:]
                print("a =",a)
            
            
            print("Expression Entered :      ",a)
            print()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            
            self.ids.list_of_steps.add_widget(Label(text="Expression entered : ", font_size = '15sp', size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= entry, font_size = '15sp', size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
            
            #String Method to look for Parentheses
            if a.count("(") == a.count(")") and a.count("(") > 0 and a.count("(") > 0:
                  i = 0
                  while i < len(a):
                    right_par = a.find(")")
                    left_par = a[:right_par].rfind("(")
                    if right_par and left_par == -1:
                        print("breaking loop, no pars")
                        break
                    range_pars = a[left_par:right_par+1]
                    range_pars = range_pars.replace("^","**")
                    print(range_pars)
                    evaled = eval(range_pars)
                    evaled = str(evaled)
                    print(evaled)
                    range_pars = range_pars.replace("**","^")
                    if a.count("(") and a.count(")") == 0:
                        print("breaking loop, a.count(()) = 0")
                        break
                    print()
                    print()
                    print("Parentheses to Solve :    ",a[:left_par],Back.GREEN,range_pars,Style.RESET_ALL,a[right_par+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Parentheses Step : " , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:left_par] + '[color=33CAFF]' + range_pars + '[/color]' + a[right_par+1:],markup=True, font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    replaced = a.replace(range_pars,evaled)
                    print()
                    print("Parentheses Solved :      ",a[:left_par],Back.GREEN,evaled,Style.RESET_ALL,a[right_par+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Parentheses Solved : " , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:left_par] + '[color=33CAFF]' + evaled + '[/color]' + a[right_par+1:],markup=True, font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    print("replaced to a:",replaced)
                    a = replaced
                    print("a =",a)
                    i = i + 1 
            
            elif a.count("(") == 0 and a.count(")") == 0:
                print("No Parenthesis, continue to exponents step")
                
            else:
                print("Parentheses Unbalanced!")
            
            
            a = a.replace(" ","")
            a = a.replace("+-","-")
            a = a.replace("-+","-")
            a = a.replace("+"," + ")
            a = a.replace("-"," - ")
            a = a.replace("**", "^")
            a = a.replace("*"," * ")
            a = a.replace("/"," / ")
            a = a.replace(" ^ - ","^-")
            a = a.replace("^*","^")
            a = a.replace("* (","(")
            a = a.replace("(","*(")
            a = a.replace("+ *(","+ (")
            a = a.replace("- *(","- (")
            a = a.replace("^*","^")
            a = a.replace("/ *","/")
            
            if a[0] == "*":
                a = a[1:]
                print("a =",a)
            
            #String Method to look for Exponents
            i = 0
            if a.count("^") > 0:
                while i < len(a):
                    carrot = a.find("^")
                    if carrot == -1:
                        break
                    print("carrot at index: ",carrot)
                    exp_right_side = a[carrot:]
                    print("exp_right_side",exp_right_side)
                    exp_right_space = exp_right_side.find(" ")
                    print("exp_right_space",exp_right_space)
                    if exp_right_space == -1:
                        exp_right_space = exp_right_side.rfind("")
                    print("exp_right_space",exp_right_space)
                    exp_right_side = a[carrot:carrot + exp_right_space]
                    print("right_side",exp_right_side)
                    exp_left_space = a[:carrot+1].rfind(" ")
                    print("left_side",exp_left_space)
                    if exp_left_space == -1:
                        exp_left_space = a[:carrot+1].find("")
                        print("left_side",exp_left_space)
                    exponent_range = a[exp_left_space:carrot + exp_right_space+1]
                    print("exp_range",exponent_range)
                    if exponent_range[:] == "-":
                        negative = exponent_range.find("-")
                        print("Negative",negative)
                        carrot_inner = exponent_range.find("^")
                        print("carrot_inner",carrot_inner)
                        exponent_left_range = exponent_range[negative:carrot_inner]
                        print("exponent_left_range",exponent_left_range)
                        exponent_left_sliced = "(" + exponent_left_range + ")"
                        exponent_range = exponent_range.replace(exponent_left_range,exponent_left_sliced)
                        print("exponent",exponent_range)
                    print("Exponent to be solved:",exponent_range)
                    exponent_range = exponent_range.replace("^","**")
                    evaled = str(eval(exponent_range))
                    exponent_range = exponent_range.replace("**","^").replace("(","").replace(")","")
                    replaced = a.replace(exponent_range,evaled)
                    print("replaced to a:",replaced)
                    print()
                    print()
                    
                    print("Exponent to Solve :       ",a[:exp_left_space],Back.GREEN,exponent_range,Style.RESET_ALL,a[carrot + exp_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Exponent Step : " , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:exp_left_space] + '[color=33CAFF]' + exponent_range + '[/color]' + a[carrot + exp_right_space+1:],markup=True, font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    print()
                    print("Exponent Sovled :         ",a[:exp_left_space],Back.GREEN,evaled,Style.RESET_ALL,a[carrot+exp_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Exponent Solved : " , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:exp_left_space] + '[color=33CAFF]' + evaled + '[/color]' + a[carrot+exp_right_space+1:],markup=True, font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    
                    a = replaced
                    a = a.replace(" ","")
                    a = a.replace("+-","-")
                    a = a.replace("-+","-")
                    a = a.replace("+"," + ")
                    a = a.replace("-"," - ")
                    a = a.replace("**", "^")
                    a = a.replace("*"," * ")
                    a = a.replace("/"," / ")
                    a = a.replace(" ^ - ","^-")
                    a = a.replace("^*","^")
                    a = a.replace("* (","(")
                    a = a.replace("(","*(")
                    a = a.replace("+ *(","+ (")
                    a = a.replace("- *(","- (")
                    a = a.replace("^*","^")
                    a = a.replace("/ *","/")
                    
                    if a[0] == "*":
                        a = a[1:]
                        print("a =",a)

                i = i + 1
            
            #String Method to look for Multiplication
            i = 0
            print(a)
            if a.count("*") > 0:
                while i < len(a):
                    a = a.replace(" * ","*")
                    print("mult",a)
                    found_mult = a.find("*")
                    if found_mult == -1:
                        break
                    print(found_mult)
                    mult_right_side = a[found_mult:]
                    print("mult_right_side",mult_right_side)
                    mult_right_space= mult_right_side.find(" ")
                    if mult_right_space == -1:
                        mult_right_space = mult_right_side.rfind("")
                    print("mult_right_found at index:",mult_right_space)
                    mult_left_side = a[:found_mult]
                    print("mult_left_side",mult_left_side)
                    mult_left_space = mult_left_side.rfind(" ")
                    if mult_left_space == -1:
                        mult_left_space = mult_left_side.find("")
                    print("mult_left_found at index:",mult_left_space)
                    mult_range = a[mult_left_space:found_mult + mult_right_space+1]
                    if mult_range == "":
                        break
                    print("mult_range",mult_range)
                    evaled = eval(mult_range)
                    print(evaled)
                    evaled = str(evaled)
                    evaled = evaled.replace("*"," * ")
                    replaced = a.replace(mult_range,evaled)
                    print("replaced to a:",replaced)
                    
                    if evaled.count("-") == 1:
                        evaled = "(" + evaled + ")"
                    
                    print()
                    print()
                    print("Multiplication to Solve : ",a[:mult_left_space],Back.GREEN,mult_range,Style.RESET_ALL,a[found_mult+mult_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Multiplication Step : " , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:mult_left_space] + '[color=33CAFF]' + mult_range + '[/color]' + a[found_mult+mult_right_space+1:],markup=True , font_size = '15sp', size_hint_y= None, height=100))
                    
                    print()
                    print("Multiplication Solved :   ", a[:mult_left_space],Back.GREEN,evaled,Style.RESET_ALL,a[found_mult+mult_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Multiplication Solved : ", font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:mult_left_space] + '[color=33CAFF]' + evaled + '[/color]'  + a[found_mult+mult_right_space+1:], markup=True, font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    a = replaced
                    a = a.replace(" ","")
                    a = a.replace("+-","-")
                    a = a.replace("-+","-")
                    a = a.replace("+"," + ")
                    a = a.replace("-"," - ")
                    a = a.replace("**", "^")
                    a = a.replace("*"," * ")
                    a = a.replace("/"," / ")
                    a = a.replace(" ^ - ","^-")
                    a = a.replace("^*","^")
                    a = a.replace("* (","(")
                    a = a.replace("(","*(")
                    a = a.replace("+ *(","+ (")
                    a = a.replace("- *(","- (")
                    a = a.replace("^*","^")
                    a = a.replace("/ *","/")
                    
                    if a[0] == "*":
                        a = a[1:]
                        print("a =",a)
   
                i = i + 1
            
            #String Method to look for Division
            i = 0
            print(a)
            if a.count("/") > 0:
                while i < len(a):
                    a = a.replace(" / ","/")
                    print("div",a)
                    found_div = a.find("/")
                    if found_div == -1:
                        break
                    print(found_div)
                    div_right_side = a[found_div:]
                    print("div_right_side",div_right_side)
                    div_right_space= div_right_side.find(" ")
                    if div_right_space == -1:
                        div_right_space = div_right_side.rfind("")
                    print("div_right_found at index:",div_right_space)
                    div_left_side = a[:found_div]
                    print("div_left_side",div_left_side)
                    div_left_space = div_left_side.rfind(" ")
                    if div_left_space == -1:
                        div_left_space = div_left_side.find("")
                    print("div_left_found at index:",div_left_space)
                    div_range = a[div_left_space:found_div + div_right_space+1]
                    if div_range == "":
                        break
                    print("div_range",div_range)
                    evaled = eval(div_range)
                    print(evaled)
                    evaled = str(evaled)
                    evaled = evaled.replace("/"," / ")
                    replaced = a.replace(div_range,evaled)
                    print("replaced to a:",replaced)
                    
                    if evaled.count("-") == 1:
                        evaled = "(" + evaled + ")"

                    print()
                    print()
                    #print("Division to Solve : ",a[:div_left_space],Back.GREEN,div_range,Style.RESET_ALL,a[found_div+div_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Division Step : " , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:div_left_space] + '[color=33CAFF]' + div_range + '[/color]' + a[found_div+div_right_space+1:],markup=True, font_size = '15sp', size_hint_y= None, height=100))
                    
                    print()
                    #print("Division Solved :   ", a[:div_left_space],Back.GREEN,evaled,Style.RESET_ALL,a[found_div+div_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Division Solved : " , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:div_left_space] + '[color=33CAFF]' + evaled + '[/color]' + a[found_div+div_right_space+1:],markup=True, font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    a = replaced
                    a = a.replace(" ","")
                    a = a.replace("+-","-")
                    a = a.replace("-+","-")
                    a = a.replace("+"," + ")
                    a = a.replace("-"," - ")
                    a = a.replace("**", "^")
                    a = a.replace("*"," * ")
                    a = a.replace("/"," / ")
                    a = a.replace(" ^ - ","^-")
                    a = a.replace("^*","^")
                    a = a.replace("* (","(")
                    a = a.replace("(","*(")
                    a = a.replace("+ *(","+ (")
                    a = a.replace("- *(","- (")
                    a = a.replace("^*","^")
                    a = a.replace("/ *","/")
                    
                    if a[0] == "*":
                        a = a[1:]
                        print("a =",a)

                i = i + 1
            
            #String Method to look for Addition
            i = 0
            while i < len(a):
                if a.count("+") > 0:
                    a = a.replace(" + ","+")
                    print("add",a)
                    found_add = a.find("+")
                    if found_add == -1:
                        break
                    print('found_add',found_add)
                    add_left = a[:found_add]
                    print('add_left',add_left)
                    add_left_space = add_left.rfind(" ")
                    print('add_left_space',add_left_space)
                    if add_left_space == -1:
                        add_left_space = add_left.find("")
                        print('add_left_space',add_left_space)
                    add_right = a[found_add+1:]
                    print('add_right',add_right)
                    add_right_space = add_right.find(" ")
                    print('add_right_space',add_right_space)
                    if add_right_space == -1:
                        add_right_space = add_right.rfind("")
                        print('add_right_space',add_right_space)
                    add_range = a[add_left_space:found_add+add_right_space+1]
                    if add_range == "":
                        break
                    print('add_range',add_range)
                    evaled = eval(add_range)
                    print('evaled',evaled)
                    evaled = str(evaled)
                    replaced = a.replace(add_range,evaled)
                    print("replaced to a:",replaced)

                    print()
                    print()
                    #print("Addition to Solve :       ",a[:add_left_space],Back.GREEN,add_range,Style.RESET_ALL,a[found_add+add_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Addition Step : " , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:add_left_space] + '[color=33CAFF]' + add_range + '[/color]' + a[found_add+add_right_space+1:],markup=True , font_size = '15sp', size_hint_y= None, height=100))
                    
                    print()
                    #print("Addition  Solved :        ",a[:add_left_space],Back.GREEN,evaled,Style.RESET_ALL,a[found_add+add_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Addition Solved : " , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:add_left_space] + '[color=33CAFF]' + evaled + '[/color]' + a[found_add+add_right_space+1:],markup=True , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    a = replaced
                    a = a.replace(" ","")
                    a = a.replace("+-","-")
                    a = a.replace("-+","-")
                    a = a.replace("+"," + ")
                    a = a.replace("-"," - ")
                    a = a.replace("**", "^")
                    a = a.replace("*"," * ")
                    a = a.replace("/"," / ")
                    a = a.replace(" ^ - ","^-")
                    a = a.replace("^*","^")
                    a = a.replace("* (","(")
                    a = a.replace("(","*(")
                    a = a.replace("+ *(","+ (")
                    a = a.replace("- *(","- (")
                    a = a.replace("^*","^")
                    a = a.replace("/ *","/")
                    
                    if a[0] == "*":
                        a = a[1:]
                        print("a =",a)

                i = i + 1
            
            #String Method to look for Subtraction
            i = 0 
            while i < len(a):
                if a.count("-") > 0:
                    a = a.replace(" - ","-")
                    print("sub",a)
                    found_sub = a.find("-")
                    if found_sub == -1:
                        break
                    print("found_sub",found_sub)
                    if found_sub == 0:
                        found_sub = a.rfind("-")
                    sub_left = a[:found_sub]
                    print("sub_left",sub_left)
                    if sub_left == "":
                        break
                    sub_left_space = sub_left.rfind(" ")
                    if sub_left_space == -1:
                        sub_left_space = sub_left.find("")
                        print("sub_left_space",sub_left_space)
                    sub_right = a[found_sub+1:]
                    print('sub_right',sub_right)
                    sub_right_space = sub_right.find(" ")
                    if sub_right_space == -1:
                        sub_right_space = sub_right.rfind("")
                        print("sub_right_space",sub_right_space)
                    sub_range = a[sub_left_space:found_sub+sub_right_space+1]
                    print("sub_range",sub_range)
                    if sub_range == "":
                        break
                    evaled = eval(sub_range)
                    print("evaled",evaled)
                    evaled = str(evaled)
                    replaced = a.replace(sub_range, evaled)
                    print("replaced to a:",replaced)
                    a = replaced
                    print("s",a)
 
                    print()
                    print()
                    #print("Subtraction to Solve :    ",a[:sub_left_space],Back.GREEN,sub_range,Style.RESET_ALL,a[found_sub+sub_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Subtraction Step : " , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:sub_left_space] + '[color=33CAFF]'  + sub_range + '[/color]' + a[found_sub+sub_right_space+1:],markup=True , font_size = '15sp', size_hint_y= None, height=100))
                    
                    print()
                    #print("Subtraction  Solved :     ",a[:sub_left_space],Back.GREEN,evaled,Style.RESET_ALL,a[found_sub+sub_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Subtraction Solved : " , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:sub_left_space] + '[color=33CAFF]'  + evaled + '[/color]'  + a[found_sub+sub_right_space+1:],markup=True , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    a = replaced
                    a = a.replace(" ","")
                    a = a.replace("+-","-")
                    a = a.replace("-+","-")
                    a = a.replace("+"," + ")
                    a = a.replace("-"," - ")
                    a = a.replace("**", "^")
                    a = a.replace("*"," * ")
                    a = a.replace("/"," / ")
                    a = a.replace(" ^ - ","^-")
                    a = a.replace("^*","^")
                    a = a.replace("* (","(")
                    a = a.replace("(","*(")
                    a = a.replace("+ *(","+ (")
                    a = a.replace("- *(","- (")
                    a = a.replace("^*","^")
                    a = a.replace("/ *","/")
                    
                    if a[0] == "*":
                        a = a[1:]
                        print("a =",a)

                i = i + 1
            a = a.replace(" ","")
            a = a.replace("e - ","e-")
            
            #print Answer with commas
            a = float(a)
            a = format(a,",")
            print()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
            print("Answer:                     ",a)
            self.ids.list_of_steps.add_widget(Label(text="Final Answer : ", font_size = '15sp', size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= a, font_size = '15sp', size_hint_y= None, height=100))

        except Exception:
            try:
                self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                    
            except Exception:               
                self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)  
                
                
class Homepage(Screen):
    pass            

class Menu(Screen):
    pass

class updates(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Menu(name="Menu"))     
sm.add_widget(PEMDAS(name="PEMDAS"))
sm.add_widget(updates(name="updates"))
sm.current = "Homepage"   

class PEMDAS(App):
    def __init__(self, **kwargs):
        super(PEMDAS, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)
    
    def _key_handler(self, instance, key, *args):
        print("key:",key)
        if key == 27:
            sm.current = sm.current
            return True
    
    def build(app):
        return sm

if __name__ == '__main__':
    PEMDAS().run()
    

