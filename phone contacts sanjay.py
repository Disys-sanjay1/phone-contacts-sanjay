class phonecontacts:

    def __init__ (self,uname,num,email):
        self.name=uname
        self.phonenumber=num
        self.emailid=email

    def phonecontact(self):
        print("phcontacts:")

    def name_verification(self):
        name=input("Enter the username:")
        print("username is:"+name)
        if type(name)==str:
            if len(name)<= 20:                                                                                #LEN FUNCTION
                print("name verified")
            else:
                raise ValueError("The name should contain only lesser than or equal to 20 letters")
        else:
            raise TypeError("The name should contain letters only")
    def emailid_verification(self):
        emailid=input("Enter the email id:")
        print("The email id is:"+emailid)
        if type(emailid) == str:
            if len(emailid) <= 30:                                                                              
                print("email_id is verified")
            else:
                raise ValueError("The Email-id should not contain more than 30 values")
        else:
            raise TypeError("Invalid email-id")

    def number_verification(self):

       phonenumber=input("Enter the phone number:")
       print("The Phone number is:"+phonenumber)
       if (len(phonenumber)==10) :
           if type(phonenumber) == int:                                                                            #TYPE VALIDATION
                print("phone-number verified")
       else:
           raise ValueError("The phone-number should not be greater than or lesser than 10")

    

sanjay=phonecontacts("sanjay",7708592085,"sanjay001",)
sanjay.phonecontact()
sanjay.name_verification()
sanjay.emailid_verification()
sanjay.number_verification()

       
