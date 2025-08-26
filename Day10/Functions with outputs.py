f_name=input("Enter the first name: ")
l_name=input("Enter the last name: ")

def format_name(f_name,l_name):
    f_formated=f_name.title()
    l_formated=l_name.title()

    return f_formated+" "+ l_formated

result= format_name(f_name,l_name)
print(result)

#ORRRRR

def format_name(f_name,l_name):
    f_format=f_name.title()
    l_format=l_name.title()

    return f_format+" "+ l_format

result= format_name(f_name ="misBA" ,l_name= "FAThiMA")
print(result)
