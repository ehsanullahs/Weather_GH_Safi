import tkinter as tk

import requests ## this will able us to communicate with live servers and get data

frame =() ## to import and use fram in our program

import PIL ## we import PIL to upload image and resize 
from PIL import Image, ImageTk

root=tk.Tk() ## we will define our refrence here and write our code 

root.title("Weather App") ## we should define our app title here 

root.geometry("600x500") ## we can define size of our window here 

#Key: @fecc68658de6ebc1257a738a307885b ## 
# this key should be provide by vendors 
##ex... ZTE Cisco Huawi,checkpoint, , in this case i have got from fallowing website
#API url: api.openweathermap.org/data/2.5/weather?q={city name}&appid-(API key)

## we are using this function through some conditaion to retrive data 

def format_response(weather):
    try:
        city=weather['name']
        condition=weather['weather'][0]['description']
        temp=weather['main']['temp']
        final_str='City:%s\nCondition:%s\nTemperature:%s'%(city,condition,temp)
    except:
        final_str='There is a problem in retrieving this information'
    return final_str
   
def get_weather(city):
    weather_key="133b5f344286719958477ade2247d8d0" ## API key for live server 
    url='https://api.openweathermap.org/data/2.5/weather' ## URL: address 
    params={"APPID":weather_key,'q':city,'units':'imperial'} ## we will pass prametrs here 
                                                   #this should be obtain from vendors as well
    response=requests.get(url,params) ## send and reccvied request by using URL and
    weather=response.json()
    print(response.json()) ## print our result ##Json is responsible for carry text over network## 
    result['text']=format_response(weather)
    
    ## access image from the path and resiszing 
img=Image.open("/Users/ehsanullahsafi/Desktop/programing/Afghanistan.png") 
img=img.resize ( (500,600) , PIL.Image.Resampling.LANCZOS) ## resize high level image to low level 
                                                           ## i have try (ANTIALIAS) its not working
img_photo=ImageTk. PhotoImage (img) ## to convert image to photo image 

bg_lbl=tk.Label(root, image=img_photo) ## we use label to display our image in background 
bg_lbl.place (x=0, y=0, width=600, height=500) ## we use this to place our image , we can use same angel size 
    
      ##we will creat heading ot image with text , 
     ## Text color will be yellow background will be red
heading_title=tk.Label(bg_lbl,text="Earth Including arounds 200,000 cities!",
fg="yellow",bg="red",font=("times new roman",17,"bold"))
    
heading_title.place(x=80,y=18)  ## place heading
    
 ## Creating and placking fram in our program
frame_one=tk.Frame(bg_lbl,bg="green",bd=5)
frame_one.place(x=80,y=60,width=450,height=50) 

 ## we will creat and place a farm

txt_box=tk.Entry(frame_one,font=("times new roman",25),width=17)
txt_box.grid(row=0,column=0,)

  ## will create botton 

btn=tk.Button(frame_one,text="Get weather Status",fg="green",font=("times new roman",
17,"bold"),command=lambda: get_weather (txt_box.get()))
btn.grid(row=0,column=1,padx=10)   
 
 ## we will create second fram  and place it on image 

frame_two=tk.Frame(bg_lbl,bg="sky blue",bd=5)
frame_two.place(x=55,y=215,width=250,height=250)
result=tk.Label(frame_two,font=40, bg='sky blue',justify='left',anchor='nw') ## our result will display on left
result.place(relwidth=1,relheight=1) ## we use this command to check result on created fram

root.mainloop()


   
   
   



 
















root.mainloop()