import customtkinter
import Page.main as Pg
import os
import pathlib

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.inpt2Val = ""
        self.opt = "Ma"
        self.path = "./Page/package.json"
        self.fullStr = ""

        self.geometry("500x300")
        self.title("Update package.json")
        self.minsize(300, 200)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0,1), weight=1)

        self.textbox = customtkinter.CTkTextbox(master=self, wrap="word")
        self.textbox.grid(row=0, column=1, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")
        self.textbox1 = customtkinter.CTkTextbox(master=self, wrap="word")
        self.textbox1.grid(row=0, column=0, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")

        self.button = customtkinter.CTkButton(master=self, command=self.button_callback, text="Get Version")
        self.button.grid(row=1, column=1, padx=20, pady=20, sticky="ew")
        
        self.button1 = customtkinter.CTkButton(master=self, command=self.button1_callback, text="Update Version", state="disabled")
        self.button1.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.combobox = customtkinter.CTkComboBox(master=self, command=self.optionMenu_callback, values=["Ma", "Mi", "Pa", "Re"])
        self.combobox.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        
        self.combobox1 = customtkinter.CTkComboBox(master=self, command=self.assign_val, values=["","Alpha", "Beta", "Release Candidate"])
        self.combobox1.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

    def button_callback(self):

        self.textbox.delete("0.0", "end")
        self.textbox.insert("insert", self.pullData("version"))

    def button1_callback(self):
        Pg.UpdateJson(self.fullStr)

    def buttonMenu_callback(self):
        
        self.textbox1.delete("0.0", "end")
        self.textbox1.insert("insert", self.fullStr)
        self.data = self.pullData()

    def optionMenu_callback(self, option):
        self.opt = option

        self.data = self.pullData()

        
        stripData = Pg.stripData(self.data, "-", "version")
        val = [i.strip() for i in stripData[0].split(".")]
        inpt = Pg.verifyStr(option, "inpt1")
        print(stripData, val, inpt, self.inpt2Val)

        if int(val[0]) == 0 or inpt != 2:
            if self.inpt2Val == "Alpha":
                if len(stripData) == 1:
                    stripData.append("a")
                    stripData.append(0)
                else:
                    self.prevVal = stripData[1]

                    if stripData[1] == "b" or stripData[1] == "rc":
                        stripData[2] = 0

                    stripData[1] = "a"

            elif self.inpt2Val == "Beta":
                if len(stripData) == 1:
                    stripData.append("b")
                    stripData.append(0)
                else:
                    self.prevVal = stripData[1]

                    if stripData[1] == "a" or stripData[1] == "rc":
                        stripData[2] = 0

                    stripData[1] = "b"

            elif self.inpt2Val == "Release Candidate":
                if len(stripData) == 1:
                    stripData.append("rc")
                    stripData.append(0)
                else:
                    self.prevVal = stripData[1]

                    if stripData[1] == "a" or stripData[1] == "b":
                        stripData[2] = 0
                    
                    stripData[1] = "rc"
        else:
            if len(stripData) > 1:
                for i in range(len(stripData)):
                    stripData.pop()
                    if len(stripData) == 1:
                        break

        

        #Indexes

        a = int(val[0])
        b = int(val[1])
        c = int(val[2])

        if len(stripData) > 1:
            d = stripData[1]
            e = int(stripData[2]) + 1
        
        if len(stripData) == 1:
            if inpt == -1 or inpt == 2:
                a += 1
                b = 0
                c = 0
            elif inpt == 0:
                b += 1
                c = 0
            elif inpt == 1:
                c += 1
        print(stripData)

        self.fullStr = Pg.retStr([a, b, c, d, e]) if len(stripData) > 1 else Pg.retStr([a, b, c])
        self.buttonMenu_callback()
        
        if self.fullStr != "":
            self.button1.configure(False, state="normal")
        else:
            self.button1.configure(False, state="disabled")



    def assign_val(self, option):
        self.inpt2Val = option
        self.optionMenu_callback(self.opt)
        self.buttonMenu_callback()
    
    def pullData(self, key = ""):
        if key != "":
            return Pg.pullData(key)
        else: 
            return Pg.pullData()

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()