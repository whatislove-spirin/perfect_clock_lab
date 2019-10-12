import tkinter 
import time
import winsound

class MyGUI:   
    def __init__(self):
        
#цвета
        self.main_bg_color = "#30302F"
        self.text_color = "#F0ECE9"
        self.button_text_color = "#ffffff"
        self.button_color = "#DF5A00"
        self.active_button = "#FF6600"
        
#размеры кнопок и текста на кнопках
        self.button_width_l = 14
        self.button_width_s = 7
        self.button_text_font = 'Helvetica 12 bold'
        
#добавочное к текущему время        
        self.additional_h = 0
        self.additional_m = 0
        
#время срабатывания будильника        
        self.alarm_hour = 0
        self.alarm_minute = 0
        self.alarm_time = ''
        
#главное окно и сопутствующие параметры       
        self.main_window = tkinter.Tk()
        self.main_window.title("Perfect clock") 
        self.main_window.geometry('600x220')
        self.main_window.configure(background=self.main_bg_color)

#фрейм для времени               
        self.top_frame = tkinter.Frame(background=self.main_bg_color)
        self.top_frame.pack(side='top')
        
#фрейм для кнопок       
        self.bottom_frame = tkinter.Frame(background=self.main_bg_color)
        self.bottom_frame.pack(side='top')
        
#текущее время        
        self.label_time = tkinter.Label(self.top_frame,
                                        font='Helvetica 84',
                                        text=f"{(int(time.strftime('%H'))+self.additional_h)%24:02d}:{(int(time.strftime('%M'))+self.additional_m)%60:02d}:{time.strftime('%S')}",
                                        bg=self.main_bg_color, fg=self.text_color)
        self.label_time.pack(side='top',padx=(11,11), pady=(12,10))
    
#кнопка перехода к установки будильника    
        self.button_alarm = tkinter.Button(self.bottom_frame,
                                           text = 'Set alarm',
                                           font = self.button_text_font,
                                           command=self.set_alarm,
                                           width=self.button_width_l, height=1,
                                           bg=self.button_color, fg =self.button_text_color, activebackground=self.active_button, activeforeground=self.main_bg_color)
        self.button_alarm.pack(side='left', padx=(7, 4),pady=(0,10))

#кнопка для добавления часа к текущему времени      
        self.button_plus_H_time = tkinter.Button(self.bottom_frame,
                                           text = '+H',
                                           font = self.button_text_font,
                                           command=self.time_plus_h,
                                           width=self.button_width_s, height=1,
                                           bg=self.button_color, fg =self.button_text_color, activebackground=self.active_button, activeforeground=self.main_bg_color)
        self.button_plus_H_time.pack(side='left', padx=(4, 4),pady=(0,10))

#кнопка для добавления минуты к текущему времени      
        self.button_plus_M_time = tkinter.Button(self.bottom_frame,
                                          text='+M',
                                          font = self.button_text_font,
                                   command=self.time_plus_m,
                                   width=self.button_width_s, height=1,
                                   bg=self.button_color, fg=self.button_text_color, activebackground=self.active_button, activeforeground=self.main_bg_color)
        self.button_plus_M_time.pack(side='left',padx=(4,4),pady=(0,10))  

#кнопка выхода из главного окна 
        self.button_quit = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          font = self.button_text_font,
                                   command=self.main_window.destroy,
                                   width=self.button_width_l, height=1,
                                   bg=self.button_color, fg=self.button_text_color, activebackground=self.active_button, activeforeground=self.main_bg_color)
        self.button_quit.pack(side='left',padx=(4,7),pady=(0,10))


    
#кнопка устанавливающая время будильника        
        self.button_alarm_confirm = tkinter.Button(self.bottom_frame,
                             text = 'Confirm',
                             font = self.button_text_font,
                             command=self.save_alarm,
                             width=self.button_width_l, height=1,
                             bg=self.button_color, fg =self.button_text_color, activebackground=self.active_button, activeforeground=self.main_bg_color)
    
#кнопка для добавления часа к будильнику     
        self.button_alarm_plus_H_time = tkinter.Button(self.bottom_frame,
                                           text = '+H',
                                           font = self.button_text_font,
                                           command=self.time_alarm_plus_h,
                                           width=self.button_width_s, height=1,
                                           bg=self.button_color, fg =self.button_text_color, activebackground=self.active_button, activeforeground=self.main_bg_color)

#кнопка для добавления минуты к будильнику      
        self.button_alarm_plus_M_time = tkinter.Button(self.bottom_frame,
                                          text='+M',
                                          font = self.button_text_font,
                                   command=self.time_alarm_plus_m,
                                   width=self.button_width_s, height=1,
                                   bg=self.button_color, fg=self.button_text_color, activebackground=self.active_button, activeforeground=self.main_bg_color)
        
#кнопка окончания редактирования будильника        
        self.button_alarm_return = tkinter.Button(self.bottom_frame,
                                          text='Return',
                                          font = self.button_text_font,
                                   command=self.return_to_clock,
                                   width=self.button_width_l, height=1,
                                   bg=self.button_color, fg=self.button_text_color, activebackground=self.active_button, activeforeground=self.main_bg_color)
    
#отображаемое время будильника   
        self.alarm_label = tkinter.Label(self.top_frame, text='00:00', font='Helvetica 84', bg=self.main_bg_color,fg=self.text_color) 
    
    
        self.label_time.after_idle(self.tick)
        self.main_window.resizable(width=False, height=False)
        self.main_window.mainloop()

#тик        
    def tick(self):
        self.label_time.after(200, self.tick)
        self.label_time['text'] = f"{(int(time.strftime('%H'))+self.additional_h)%24:02d}:{(int(time.strftime('%M'))+self.additional_m)%60:02d}:{time.strftime('%S')}"
        if self.alarm_time == (f"{(int(time.strftime('%H'))+self.additional_h)%24:02d}:{(int(time.strftime('%M'))+self.additional_m)%60:02d}"):
            self.alarm_A()
            
#перейти от часов к будильнику            
    def set_alarm(self):
        self.label_time.pack_forget()
        self.alarm_label.pack(side='top',padx=(11,11), pady=(12,10))

#спрятать кнопки основного окна      
        self.button_alarm.pack_forget()
        self.button_plus_H_time.pack_forget()
        self.button_plus_M_time.pack_forget()
        self.button_quit.pack_forget()
        
#показать кнопки редактирования будильника
        self.button_alarm_confirm.pack(side='left', padx=(7, 4),pady=(0,10))
        self.button_alarm_plus_H_time.pack(side='left', padx=(4, 4),pady=(0,10))
        self.button_alarm_plus_M_time.pack(side='left',padx=(4,4),pady=(0,10))
        self.button_alarm_return.pack(side='left',padx=(4,7),pady=(0,10))
        
#добавить час к часам
    def time_plus_h(self):
        self.additional_h += 1
        
#добавить минуту к часам
    def time_plus_m(self):
        self.additional_m += 1
        
#добавить час к будильнику        
    def time_alarm_plus_h(self):
        self.alarm_hour = (self.alarm_hour+1)%24
        self.alarm_label['text'] = f"{self.alarm_hour%24:02d}:{self.alarm_minute:02d}"

#добавить минуту к будильнику
    def time_alarm_plus_m(self):
        self.alarm_minute = (self.alarm_minute+1)%60
        self.alarm_label['text'] = f"{self.alarm_hour:02d}:{self.alarm_minute%60:02d}"

#перейти от будильника к часам
    def return_to_clock(self):
        self.alarm_label.pack_forget()
        self.label_time.pack(side='top',padx=(11,11), pady=(12,10))

#спрятать кнопки редактирования будильника
        self.button_alarm_confirm.pack_forget()
        self.button_alarm_plus_H_time.pack_forget()
        self.button_alarm_plus_M_time.pack_forget()
        self.button_alarm_return.pack_forget()

#показать кнопки основного окна
        self.button_alarm.pack(side='left', padx=(7, 4),pady=(0,10))
        self.button_plus_H_time.pack(side='left', padx=(4, 4),pady=(0,10))
        self.button_plus_M_time.pack(side='left',padx=(4,4),pady=(0,10))
        self.button_quit.pack(side='left',padx=(4,7),pady=(0,10))

#сохранение времени будильника
    def save_alarm(self):
        self.alarm_time = self.alarm_label['text']

#сигнал будильника  
    def alarm_A(self):
         winsound.Beep(1000, 500)
                 
my_gui = MyGUI()