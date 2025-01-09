class student:

    def_init_(self,name,hodname,college):
    self.name=name
    self.hodname=hodname
    self.college=college
    def getdata(self):
        self.name=input('enter the student name')
        class hod(student):
            def data(self):
                self.hodname=input('enter the hodname')
                def putdata(self):
                    self.college=input('enter college')
                    def display(self):
                        print('student name is',self.name)
                        print('your hodname is',self.hodename)
                        print(' college name is',self.college)
                        obj=hod('','','')
                        obj.getdata()
                        obj.data1()
                        obj.putdata()
                        obj.display()