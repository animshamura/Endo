# ~ sample project on student data recieving ~
# ~ Author - Shamura Ahmad ~

bcl = []
cl1 = []; cl2 = []; cl3 = []; cl4 = []; cl5  = []
cl6 = []; cl7 = []; cl8 = []; cl9 = []; cl10 = []
bcl.append(cl1); bcl.append(cl2); bcl.append(cl3); bcl.append(cl4);
bcl.append(cl5); bcl.append(cl6); bcl.append(cl7); bcl.append(cl8);
bcl.append(cl9); bcl.append(cl10)

class Student:
  def StudentName(self,sn):
    self.sn=sn
  def ParentName1(self,pn1):
    self.pn1=pn1
  def ParentName2(self,pn2):
    self.pn2=pn2
  def Address1(self,ad1):
    self.ad1=ad1
  def Address2(self,ad2):
    self.ad2=ad2
  def PhoneNumber(self,ph):
    self.ph=ph
  def GetStudentName(self):
    return self.sn
  def GetParentName1(self):
    return self.pn1
  def GetParentName2(self):
    return self.pn2
  def GetAddress1(self):
    return self.ad1
  def GetAddress2(self):
    return self.ad2
  def GetPhoneNumber(self):
    return self.ph
  

while(True):
    print(" *** enter 1 for new entry *** \n *** enter 2 for query old ones ** ")
    t = int(input())
    if(t==1):
      print(" *** enter class to get entry *** ")
      c = int(input())
      St = Student()
      print(" *** enter student's name *** ")
      St.StudentName(input())
      print(" *** enter student's father's name *** ")
      St.ParentName1(input())
      print(" *** enter student's mother's name *** ")
      St.ParentName2(input())
      print(" *** enter student's present address *** ")
      St.Address1(input())
      print(" *** enter student's permanent address *** ")
      St.Address2(input())
      print(" *** enter student's phone number *** ")
      St.PhoneNumber(input()) 
      if(c==1):  
       cl1.append(St)
      elif(c==2): 
       cl2.append(St)
      elif(c==3):
       cl3.append(St)
      elif(c==4): 
       cl4.append(St)
      elif(c==5):
       cl5.append(St)
      elif(c==6): 
       cl6.append(St)
      elif(c==7): 
       cl7.append(St)
      elif(c==8): 
       cl8.append(St)
      elif(c==9): 
       cl9.append(St)
      else: 
       cl10.append(St)
      print("\n *** info added successfully *** \n")
    
    else:
        print(" *** enter class to inquery *** ")
        c1 = int(input())
        cl = bcl[c1-1]
        print(" *** enter student's name for inquery *** ")
        n1 = input()
        inf = "Not Found!" 
        for i in cl:
          if(i.GetStudentName()==n1):
            inf = "Found!"
          if(inf=="Found!"):
            print("\nStudent's Name    : "+i.GetStudentName())
            print("Father's Name     : "+i.GetParentName1())
            print("Mother's Name     : "+i.GetParentName2())
            print("Present Address   : "+i.GetAddress1())
            print("Permanent Address : "+i.GetAddress2())
            print("Phone Number      : "+i.GetPhoneNumber()+"\n")
            break 
        if(inf=="Not Found!"):
          print("Student Not Found!\n")
    if(int(input(" *** enter 0 to exit, else to continue ***\n"))==0): break

      




  
  
     
