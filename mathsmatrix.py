# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 18:49:50 2021

@author: user
"""

def main():
    i=1
    while i==1:
        print("How can we help you?")
        print("1.Calculator")
        print("2.Convertor")
        print("3.Statistics")
        print("4.Mensuration")
        print("5.Quit")
        ch=int(input("Enter your choice here: "))
        if ch==1:
            calculator()
            i=0
        elif ch==2:
            convertor()
            i=0
        elif ch==3:
            statistics()
            i=0
        elif ch==4:
            mensuration()
            i=0
        elif ch==5:
            print("Thank you for visiting!!!")
            i=0
        else: 
            print("Invalid choice... Please re-enter your choice :")
            i=1 

def calculator():
    import math
    i=1
    while i==1:
        print("Which operation would you like to perform:")
        print("1.Sum\n2.Subtract\n3.Product\n4.Division\n5.Modulus(Remainder)\n6.Sine\n7.Cosine\n8.Tangent\n9.Log10\n10.Power\n11.Square Root\n12.Back to Home\n13.Quit")
        ch1=int(input("Enter your choice here:"))
        if ch1==1 or ch1==2 or ch1==3 or ch1==4 or ch1==5:
            a=float(input("Enter the first number for operation:"))
            b=float(input("Enter the second number for operation:"))
            if ch1==1:
                print("Sum=",(a+b))
            elif ch1==2:
                print("Difference=",(a-b))
            elif ch1==3:
                print("Product=",(a*b))
            elif ch1==4:
                print("Division=",(a/b))
            elif ch1==5:
                print("Modulus(Remainder)=",(a%b))
            con=input("Do you want to continue:(y for yes/any other key for no):")
            if con=='y' or con=='Y':
                ch1=int(input("Enter\n1.Back\n2.Back to Home"))
                if ch1==1:
                    i=1
                elif ch1==2:
                    i=0
                    main()
            else:
                i=0
                print("Thank you for visiting!!!")
        elif ch1==6 or ch1==7 or ch1==8 or ch1==9 or ch1==11:
            a=float(input("Enter the value on which the operation is to be performed:"))
            if ch1==6:
                print("Sine(",a,"):",math.sin(a))
            elif ch1==7:
                print("Cosine(",a,"):",math.cos(a))
            elif ch1==8:
                print("Tangent(",a,"):",math.tan(a))
            elif ch1==9:
                print("Log10(",a,"):",math.log(a))
            elif ch1==11:
                print("Square Root(",a,"):",math.sqrt(a))
            con=input("Do you want to continue:(y for yes/any other key for no):")
            if con=='y' or con=='Y':
                ch1=int(input("Enter\n1.Back\n2.Back to Home"))
                if ch1==1:
                    i=1
                elif ch1==2:
                    i=0
                    main()
            else:
                i=0
                print("Thank you for visiting!!!")
        elif ch1==10:
            a=float(input("Enter the base:"))
            b=float(input("Enter the power:"))
            while a<0:
                a=float(input("Enter the base:(Base less than 0 is not allowed)"))
            print("Power=",(a**b))
            con=input("Do you want to continue:(y for yes/any other key for no):")
            if con=='y' or con=='Y':
                ch1=int(input("Enter\n1.Back\n2.Back to Home"))
                if ch1==1:
                    i=1
                elif ch1==2:
                    i=0
                    main()
            else:
                i=0
                print("Thank you for visiting!!!")
        elif ch1==12:
            i=0
            main()
        elif ch1==13:
            i=0
            print("Thank You for visiting!!!")
        else:
            i=1
            print("Invalid choice... Please re-enter your choice:")

def convertor():
    i=1
    while i==1:
        print("Which type of conversion you wish to do:")
        print("1.Currency Convertor\n2.Unit Convertor\n3.Back to Home\n4.Quit")
        ch2=int(input("Enter your choice here:"))
        if ch2==1:
            currency()
            i=0
        elif ch2==2:
            unit()
            i=0
        elif ch2==3:
            main()
            i=0
        elif ch2==4:
            print("Thank you for visiting!!!")
            i=0
        else:
            print("Invalid choice... Please re-enter your choice :")
            i=1        

def statistics():
    i=1
    while i==1:
        print("Which chart would you like to create:")
        print("1.Bar Graph\n2.Histogram\n3.Scatter Plot\n4.Pie Chart\n5.Back to Home\n6.Quit")
        ch3=int(input("Enter your choice here:"))
        if ch3==1:
            bar()
            i=0
        elif ch3==2:
            hist()
            i=0
        elif ch3==3:
            scatter()
            i=0
        elif ch3==4:
            pie()
            i=0
        elif ch3==5:
            main()
            i=0
        elif ch3==6:
            print("Thank you for visiting!!!")
            i=0
        else: 
            print("Invalid choice... Please re-enter your choice :")
            i=1 

def mensuration():
    i=1
    while i==1:
        print("Which shape would you like to find Area/Perimeter/Volume")
        print("1.Circle\n2.Triangle\n3.Rectangle\n4.Square\n5.Solid Cylinder\n6.Cube\n7.Sphere\n8.Cone\n9.Back to Home\n10.Quit")
        m=int(input("Enter your choice here:"))
        if m>0 and m<9:
            if m==1:
                r=float(input("Enter the radius of circle:"))
                print("Area of cirle=",(3.14*r*r),"\nPerimeter of circle=",(2*3.14*r))
                i=0
            elif m==2:
                i=0
                s1=float(input("Enter the length of the base of the triangle:"))
                s2=input("Enter length of second side of the triangle(if known):")
                s3=input("Enter length of third side of the triangle(if known):")
                h=input("Enter the length of the height of the triangle(if known):")
                if s2:
                    s2=float(s2)
                    if s3:
                        s3=float(s3)
                        if h:
                            float(h)
                            print("Area of triangle=",(0.5*s1*h),"\nPerimeter of triangle=",(s1+s2+s3))
                        else:
                            print("Perimeter of triangle=",(s1+s2+s3))
                elif h:
                    h=float(h)
                    print("Area of triangle=",(0.5*s1*h))
                else:
                    print("Incomplete input... Please try again...")
            elif m==3:
                i=0
                l=float(input("Enter the length of rectangle:"))
                b=float(input("Enter the breadth of rectangle:"))
                print("Area of rectangle=",(l*b),"\nPerimeter of rectangle=",(2*(l+b)))
            elif m==4:
                i=0
                a=float(input("Enter the side of square:"))
                print("Area of square=",(a*a),"\nPerimeter of square=",(4*a))
            elif m==5:
                i=0
                r=float(input("Enter the radius of solid cylinder:"))
                h=float(input("Enter the height of solid cylinder:"))
                print("Volume of solid cylinder=",(3.14*r*r*h),"\nCurved surface area of sloid cylinder=",(2*3.14*r*h),"\nTotal Surface Area of Solid Cylinder=",((2*3.14*r*r)+(2*3.14*r*h)))
            elif m==6:
                i=0
                s=float(input("Enter the side of cube:"))
                print("Volume of cube=",(s*s*s),"\nLateral surface area of cube=",(4*s*s),"\nTotal surface area of cube=",(6*s*s))
            elif m==7:
                i=0
                r=float(input("Enter the radius of sphere:"))
                print("Volume of sphere=",(4*3.14*r**3),"Total surface area of sphere=",(4*3.14*r*r))
            elif m==8:
                i=0
                r=float(input("Enter the radius of the cone:"))
                l=input("Enter the slant height of the cone(if known):")
                h=input("Enter the height of the cone(if known):")
                if l:
                    l=float(l)
                    if h:
                        h=float(h)
                        print("Volume of cone=",((3.14*r*r*h)/3),"\nCurved surface area of cone=",(3.14*r*l),"\nTotal surface area of cone=",((3.14*r*l)+(3.14*r*r)))
                    else:
                        print("Curved surface area of cone=",(3.14*r*l),"\nTotal surface area of cone=",((3.14*r*l)+(3.14*r*r)))
                elif h:
                    h=float(h)
                    print("Volume of cone=",((3.14*r*r*h)/3))
                else:
                    print("Incomplete input... Please try again...")
            con=input("Do you want to continue:(y for yes/any other key for no):")
            if con=='y' or con=='Y':
                ch1=int(input("Enter\n1.Back\n2.Back to Home"))
                if ch1==1:
                    i=1
                elif ch1==2:
                    i=0
                    main()
            else:
                i=0
                print("Thank you for visiting!!!")
        elif m==9:
            main()
            i=0
        elif m==10:
            i=0
            print("Thank you for visiting!!!")
        else:
            i=1
            print("Invalid choice... Please re-enter your choice:")    

def currency():
    i=1
    while i==1:
        print("Which currency you want to convert:")
        print("1.US Dollar(USD)\n2.Euro(EUR)\n3.Japanese Yen(JPY)\n4.British Pound(GBP)\n5.Australian Dollar(AUD)\n6.Canadian Dollar(CAD)\n7.Swiss Franc(CHF)\n8.Indian Ruppee(INR)\n9.Swedish Krona(SEK)\n10.Russian Ruble(RUB)\n11.Back\n12.Back to Home\n13.Quit")
        cu1=int(input("Enter your choice here:"))
        if cu1>0 and cu1<11:
            cu2=int(input("Enter the currency into which you want to convert:"))
        if (cu1<11 and cu1>0) and (cu2<11 and cu2>0):
            i=0
            amt=int(input("Enter the amount you want to convert:"))
            if cu1==1:
                if cu2==1:
                    print("USD=",(amt))
                elif cu2==2:
                    print("EUR=",(amt*0.90))
                elif cu2==3:
                    print("JPY=",(amt*109.38))
                elif cu2==4:
                    print("GBP=",(amt*0.773))
                elif cu2==5:
                    print("AUD=",(amt*1.445))
                elif cu2==6:
                    print("CAD=",(amt*1.315))
                elif cu2==7:
                    print("CHF=",(amt*0.982))
                elif cu2==8:
                    print("INR=",(amt*71.19))
                elif cu2==9:
                    print("SEK=",(amt*9.442))
                elif cu2==10:
                    print("RUB=",(amt*63.921))
            elif cu1==2:
                if cu2==1:
                    print("USD=",(amt*1.109))
                elif cu2==2:
                    print("EUR=",(amt))
                elif cu2==3:
                    print("JPY=",(amt*121.324))
                elif cu2==4:
                    print("GBP=",(amt*0.857))
                elif cu2==5:
                    print("AUD=",(amt*1.603))
                elif cu2==6:
                    print("CAD=",(amt*1.459))
                elif cu2==7:
                    print("CHF=",(amt*1.089))
                elif cu2==8:
                    print("INR=",(amt*78.957))
                elif cu2==9:
                    print("SEK=",(amt*10.472))
                elif cu2==10:
                    print("RUB=",(amt*70.895))
            elif cu1==3:
                if cu2==1:
                    print("USD=",(amt*0.0091))
                elif cu2==2:
                    print("EUR=",(amt*0.0082))
                elif cu2==3:
                    print("JPY=",(amt))
                elif cu2==4:
                    print("GBP=",(amt*0.007))
                elif cu2==5:
                    print("AUD=",(amt*0.0132))
                elif cu2==6:
                    print("CAD=",(amt*0.012))
                elif cu2==7:
                    print("CHF=",(amt*0.0089))
                elif cu2==8:
                    print("INR=",(amt*0.6507))
                elif cu2==9:
                    print("SEK=",(amt*0.0863))
                elif cu2==10:
                    print("RUB=",(amt*0.5843))
            elif cu1==4:
                if cu2==1:
                    print("USD=",(amt*1.2935))
                elif cu2==2:
                    print("EUR=",(amt*1.1662))
                elif cu2==3:
                    print("JPY=",(amt*141.496))
                elif cu2==4:
                    print("GBP=",(amt))
                elif cu2==5:
                    print("AUD=",(amt*1.869))
                elif cu2==6:
                    print("CAD=",(amt*1.7014))
                elif cu2==7:
                    print("CHF=",(amt*1.2703))
                elif cu2==8:
                    print("INR=",(amt*92.0842))
                elif cu2==9:
                    print("SEK=",(amt*12.2136))
                elif cu2==10:
                    print("RUB=",(amt*82.6824))
            elif cu1==5:
                if cu2==1:
                    print("USD=",(amt*0.6919))
                elif cu2==2:
                    print("EUR=",(amt*0.6239))
                elif cu2==3:
                    print("JPY=",(amt*75.6978))
                elif cu2==4:
                    print("GBP=",(amt*0.5349))
                elif cu2==5:
                    print("AUD=",(amt))
                elif cu2==6:
                    print("CAD=",(amt*0.9102))
                elif cu2==7:
                    print("CHF=",(amt*0.6796))
                elif cu2==8:
                    print("INR=",(amt*49.26))
                elif cu2==9:
                    print("SEK=",(amt*6.534))
                elif cu2==10:
                    print("RUB=",(amt*44.23))
            elif cu1==6:
                if cu2==1:
                    print("USD=",(amt*0.7602))
                elif cu2==2:
                    print("EUR=",(amt*0.68))
                elif cu2==3:
                    print("JPY=",(amt*83.16))
                elif cu2==4:
                    print("GBP=",(amt*0.587))
                elif cu2==5:
                    print("AUD=",(amt*1.0985))
                elif cu2==6:
                    print("CAD=",(amt))
                elif cu2==7:
                    print("CHF=",(amt*0.7466))
                elif cu2==8:
                    print("INR=",(amt*54.12))
                elif cu2==9:
                    print("SEK=",(amt*7.1782))
                elif cu2==10:
                    print("RUB=",(amt*48.59))
            elif cu1==7:
                if cu2==1:
                    print("USD=",(amt*1.0182))
                elif cu2==2:
                    print("EUR=",(amt*0.918))
                elif cu2==3:
                    print("JPY=",(amt*111.383))
                elif cu2==4:
                    print("GBP=",(amt*0.7871))
                elif cu2==5:
                    print("AUD=",(amt*1.4714))
                elif cu2==6:
                    print("CAD=",(amt*1.3393))
                elif cu2==7:
                    print("CHF=",(amt))
                elif cu2==8:
                    print("INR=",(amt*72.487))
                elif cu2==9:
                    print("SEK=",(amt*9.6143))
                elif cu2==10:
                    print("RUB=",(amt*65.0865))
            elif cu1==8:
                if cu2==1:
                    print("USD=",(amt*0.014))
                elif cu2==2:
                    print("EUR=",(amt*0.0126))
                elif cu2==3:
                    print("JPY=",(amt*1.5365))
                elif cu2==4:
                    print("GBP=",(amt*0.0108))
                elif cu2==5:
                    print("AUD=",(amt*0.0202))
                elif cu2==6:
                    print("CAD=",(amt*0.0184))
                elif cu2==7:
                    print("CHF=",(amt*0.0137))
                elif cu2==8:
                    print("INR=",(amt))
                elif cu2==9:
                    print("SEK=",(amt*0.1326))
                elif cu2==10:
                    print("RUB=",(amt*0.8978))
            elif cu1==9:
                if cu2==1:
                    print("USD=",(amt*0.1059))
                elif cu2==2:
                    print("EUR=",(amt*0.0954))
                elif cu2==3:
                    print("JPY=",(amt*11.585))
                elif cu2==4:
                    print("GBP=",(amt*0.0818))
                elif cu2==5:
                    print("AUD=",(amt*0.153))
                elif cu2==6:
                    print("CAD=",(amt*0.14))
                elif cu2==7:
                    print("CHF=",(amt*0.10))
                elif cu2==8:
                    print("INR=",(amt*7.5394))
                elif cu2==9:
                    print("SEK=",(amt))
                elif cu2==10:
                    print("RUB=",(amt*6.58))
            elif cu1==10:
                if cu2==1:
                    print("USD=",(amt*0.016))
                elif cu2==2:
                    print("EUR=",(amt*0.015))
                elif cu2==3:
                    print("JPY=",(amt*1.77))
                elif cu2==4:
                    print("GBP=",(amt*0.012))
                elif cu2==5:
                    print("AUD=",(amt*0.023))
                elif cu2==6:
                    print("CAD=",(amt*0.021))
                elif cu2==7:
                    print("CHF=",(amt*0.01536))
                elif cu2==8:
                    print("INR=",(amt*1.15))
                elif cu2==9:
                    print("SEK=",(amt*0.15))
                elif cu2==10:
                    print("RUB=",(amt))
            con=input("Do you want to continue:(y for yes/any other key for no):")
            if con=='y' or con=='Y':
                ch1=int(input("Enter\n1.Back\n2.Back to Home"))
                if ch1==1:
                    i=0
                    convertor()
                elif ch1==2:
                    i=0
                    main()
            else:
                i=0
                print("Thank you for visiting!!!")
        elif cu1==11:
            i=0
            convertor()
        elif cu1==12:
            i=0
            main()
        elif cu1==13:
            i=0
            print("Thank you for visiting!!!")
        else:
            i=1
            print("Inavlid choice...Please re-enter ")

def unit():
    i=1
    while i==1:
        print("Which conversion you want to perform:")
        print(" 1.length\n2.time\n3.weight\n4.back\n5.back to home\n6.quit")
        s=int(input("Enter your choice"))
        if s==1:
            i=0
            print("1.m to km\n2.m to inch\n3.m to foot\n4. m to cm\n5.km to m\n6.km to inch\n7.km to foot\n8.inch to m\n9.inch to km\n10.inch to foot\n11.foot to m\n12.foot to km\n13.foot to inch\n14.quit")
            p=int(input("enter your choice"))
            x=int(input("enter the value you want to convert"))
            if p==1:
                a=x*1000000
                print("your conversion ans is",a)
            elif p==2:
                a=x*39.37
                print("your conversion ans is",a)
            elif p==3:
                a=x*3.28
                print("your conversion ans is",a)
            elif p==4:
                a=x*100
                print("your conversion ans is",a)
            elif p==5:
                a=x*1000
                print("your conversion ans is",a)
            elif p==6:
                a=x*39370
                print("your conversion ans is",a)
            elif p==7:
                a=x*3280.83
                print("your conversion ans is",a)
            elif p==8:
                a=x/39.37
                print("your conversion ans is",a)
            elif p==9:
                a=x/39370
                print("your conversion ans is",a)
            elif p==10:
                a=x/12
                print("your conversion ans is",a)
            elif p==11:
                a=x/3.281
                print("your conversion ans is",a)
            elif p==13:
                a=x*12
                print("your conversion ans is",a)
            elif p==12:
                a=x/3281
                print("your conversion ans is",a)
            elif p==14:
                print("Thank you for visiting!!!")    
            con=input("Do you want to continue:(y for yes/any other key for no):")
            if con=='y' or con=='Y':
                ch1=int(input("Enter\n1.Back\n2.Back to Home"))
                if ch1==1:
                    i=0
                    convertor()
                elif ch1==2:
                    i=0
                    main()
            else:
                i=0
                print("Thank you for visiting!!!")
        elif s==2:
            i=0
            print("1.sec to min\n2.sec to hr\n3.min to sec\n4.min to hr\n5.hr to sec\n6.hr to min\n7.quit")
            y=int(input("enter your choice:"))
            x=int(input("enter the value you want to convert:"))
            if y==1:
               a=x/60
               print("your conversion ans is:",a)
            elif y==2:
               a=x/3600
               print("your conversion ans is:",a)
            elif y==3:
                a=x*60
                print("your conversion ans is:",a)
            elif y==4:
                a=x/60
                print("your conversion ans is:",a)
            elif y==5:
                a=x*3600
                print("your conversion ans is:",a)
            elif y==6:
                a=x*60
                print("your conversion ans is:",a)
            elif y==7:
                print("Thank you for visiting!!!")
            con=input("Do you want to continue:(y for yes/any other key for no):")
            if con=='y' or con=='Y':
                ch1=int(input("Enter\n1.Back\n2.Back to Home"))
                if ch1==1:
                    i=0
                    convertor()
                elif ch1==2:
                    i=0
                    main()
            else:
                i=0
                print("Thank you for visiting!!!")

        elif s==3:
            i=0
            print("1.kg to gm\n2.kg to tonnes\n3.kg to ounce\n4.gm to kg\n5.gm to ounce\n6.ounnce to gm\n7.ounce to tonnes\n8.ounce to kg\n9.quit" )
            z=int(input("enter your choice"))
            x=int(input("enter the value you want to convert"))
            if z==1:
                a=x*1000
                print("your ans is",a)
            elif z==2:
                a=x/1000
                print("your ans is ",a)
            elif z==3:
                a=x*35.27
                print("your ans is ",a)
            elif z==4:
                a=x/1000
                print("your ans is ",a)
            elif z==5:
                 a=x/35274
                 print("your ans is ",a)
            elif z==6:
                a=x*28.35
                print("your ans is ",a)
            elif z==7:
                a=x/35274
                print("your ans is ",a)
            elif z==8:
                 a=x/35.274
                 print("your ans is ",a)
            elif z==9:
                print("Thank you for visiting!!!")
            con=input("Do you want to continue:(y for yes/any other key for no):")
            if con=='y' or con=='Y':
                ch1=int(input("Enter\n1.Back\n2.Back to Home"))
                if ch1==1:
                    i=0
                    convertor()
                elif ch1==2:
                    i=0
                    main()
            else:
                i=0
                print("Thank you for visiting!!!")
        elif s==4:
            convertor()
            i=0
        elif s==5 :
            main()
            i=0
        elif s==6:
            print("Thank you for visiting!!!")
            i=0
        else:
            i=1
            print("Invalid choice... Please renter your choice:")

def bar():
    n=int(input("Enter the NUMBER of entries you want to display in the bar graph:"))
    for i in range(1,(n+1)):
        x=int(input("Enter the value on x-axis:"))
        y=int(input("Enter the value on y-axis:"))
        plt.bar([x],[y],label="")
    xlab=input("Enter the label for x-axis(if any):")
    ylab=input("Enter the label for y-axis(if any):")
    if xlab:
        plt.xlabel(xlab)
    else:
        plt.xlabel("X-Axis")
    if ylab:
        plt.ylabel(ylab)
    else:
        plt.ylabel("Y-Axis")
    title=input("Enter the title of the graph(if any):")
    if title:
        plt.title(title)
    else:
        plt.title("Bar Graph")
    plt.legend()
    plt.show()
    con=input("Do you want to continue:(y for yes/any other key for no):")
    if con=='y' or con=='Y':
        ch1=int(input("Enter\n1.Back\n2.Back to Home"))
        if ch1==1:
            statistics()
        elif ch1==2:
            main()
    else:
        print("Thank you for visiting!!!")

def hist():
    x=[0]
    y=[]
    n=int(input("Enter the NUMBER of entries you want to display in the histogram:"))
    for i in range(1,(n+1)):
        x1=int(input("Enter the value on x-axis:"))
        y1=int(input("Enter the value on y-axis:"))
        x.append(x1)
        y.append(y1)
    plt.hist(y,x,histtype='bar')
    xlab=input("Enter the label for x-axis(if any):")
    ylab=input("Enter the label for y-axis(if any):")
    if xlab:
        plt.xlabel(xlab)
    else:
        plt.xlabel("X-Axis")
    if ylab:
        plt.ylabel(ylab)
    else:
        plt.ylabel("Y-Axis")
    title=input("Enter the title of the graph(if any):")
    if title:
        plt.title(title)
    else:
        plt.title("Histogram")
    plt.legend()
    plt.show()
    con=input("Do you want to continue:(y for yes/any other key for no):")
    if con=='y' or con=='Y':
        ch1=int(input("Enter\n1.Back\n2.Back to Home"))
        if ch1==1:
            statistics()
        elif ch1==2:
            main()
    else:
        print("Thank you for visiting!!!")

def scatter():
    x=[]
    y=[]
    n=int(input("Enter the NUMBER of entries you want to display in the Scatter plot:"))
    for i in range(1,(n+1)):
        x1=int(input("Enter the value on x-axis:"))
        y1=int(input("Enter the value on y-axis:"))
        x.append(x1)
        y.append(y1)
    plt.scatter(x,y,s=25,marker='o')
    xlab=input("Enter the label for x-axis(if any):")
    ylab=input("Enter the label for y-axis(if any):")
    if xlab:
        plt.xlabel(xlab)
    else:
        plt.xlabel("X-Axis")
    if ylab:
        plt.ylabel(ylab)
    else:
        plt.ylabel("Y-Axis")
    title=input("Enter the title of the graph(if any):")
    if title:
        plt.title(title)
    else:
        plt.title("Scatter Plot")
    plt.legend()
    plt.show()
    con=input("Do you want to continue:(y for yes/any other key for no):")
    if con=='y' or con=='Y':
        ch1=int(input("Enter\n1.Back\n2.Back to Home"))
        if ch1==1:
            statistics()
        elif ch1==2:
            main()
    else:
        print("Thank you for visiting!!!")

def pie():
    n=int(input("Enter the NUMBER of parts you want to display in pie chart:"))
    slices,activity,exp=[],[],[]
    for i in range(1,(n+1)):
        print("Enter the value of part",i,end="")
        slice=int(input(""))
        slices.append(slice)
        act=input("Enter the corresponding activity to be displayed in the pie chart:")
        activity.append(act)
        exp.append(0)
    plt.pie(slices,labels=activity,startangle=90,shadow=True,explode=exp,autopct='%1.1f%%')
    title=input("Enter the title of the graph(if any):")
    if title:
        plt.title(title)
    else:
        plt.title("Pie Chart")
    plt.show()
    con=input("Do you want to continue:(y for yes/any other key for no):")
    if con=='y' or con=='Y':
        ch1=int(input("Enter\n1.Back\n2.Back to Home"))
        if ch1==1:
            statistics()
        elif ch1==2:
            main()
    else:
        print("Thank you for visiting!!!")

# 
import matplotlib.pyplot as plt
plt.plot([1,1,3.5,6,6],[1,7,4,7,1])
plt.plot([7,9.5,12,11,8],[1,7,1,4,4])
plt.plot([13,18,15.5,15.5],[7,7,7,1])
plt.plot([19,19,19,24,24,24],[7,1,4,4,7,1])
plt.plot([30,25,25,30,30,25],[7,7,4,4,1,1])
plt.plot([38,38,43],[7,1,1])
plt.plot([44,46.5,49,48,45],[1,7,1,4,4])
plt.plot([50,50,55,55,50,55,55,50],[1,7,7,4,4,4,1,1])
plt.show()
print("Hi Guys... Welcome to MATHS LAB...")
main()
def main():
    i=1
    while i==1:
        print("How can we help you?")
        print("1.Calculator")
        print("2.Convertor")
        print("3.Statistics")
        print("4.Mensuration")
        print("5.Quit")
        ch=int(input("Enter your choice here: "))
        if ch==1:
            calculator()
            i=0
        elif ch==2:
            convertor()
            i=0
        elif ch==3:
            statistics()
            i=0
        elif ch==4:
            mensuration()
            i=0
        elif ch==5:
            print("Thank you for visiting!!!")
            i=0
        else: 
            print("Invalid choice... Please re-enter your choice :")
            i=1 

def calculator():
    import math
    i=1
    while i==1:
        print("Which operation would you like to perform:")
        print("1.Sum\n2.Subtract\n3.Product\n4.Division\n5.Modulus(Remainder)\n6.Sine\n7.Cosine\n8.Tangent\n9.Log10\n10.Power\n11.Square Root\n12.Back to Home\n13.Quit")
        ch1=int(input("Enter your choice here:"))
        if ch1==1 or ch1==2 or ch1==3 or ch1==4 or ch1==5:
            a=float(input("Enter the first number for operation:"))
            b=float(input("Enter the second number for operation:"))
            if ch1==1:
                print("Sum=",(a+b))
            elif ch1==2:
                print("Difference=",(a-b))
            elif ch1==3:
                print("Product=",(a*b))
            elif ch1==4:
                print("Division=",(a/b))
            elif ch1==5:
                print("Modulus(Remainder)=",(a%b))
            con=input("Do you want to continue:(y for yes/any other key for no):")
            if con=='y' or con=='Y':
                ch1=int(input("Enter\n1.Back\n2.Back to Home"))
                if ch1==1:
                    i=1
                elif ch1==2:
                    i=0
                    main()
            else:
                i=0
                print("Thank you for visiting!!!")
        elif ch1==6 or ch1==7 or ch1==8 or ch1==9 or ch1==11:
            a=float(input("Enter the value on which the operation is to be performed:"))
            if ch1==6:
                print("Sine(",a,"):",math.sin(a))
            elif ch1==7:
                print("Cosine(",a,"):",math.cos(a))
            elif ch1==8:
                print("Tangent(",a,"):",math.tan(a))
            elif ch1==9:
                print("Log10(",a,"):",math.log(a))
            elif ch1==11:
                print("Square Root(",a,"):",math.sqrt(a))
            con=input("Do you want to continue:(y for yes/any other key for no):")
            if con=='y' or con=='Y':
                ch1=int(input("Enter\n1.Back\n2.Back to Home"))
                if ch1==1:
                    i=1
                elif ch1==2:
                    i=0
                    main()
            else:
                i=0
                print("Thank you for visiting!!!")
        elif ch1==10:
            a=float(input("Enter the base:"))
            b=float(input("Enter the power:"))
            while a<0:
                a=float(input("Enter the base:(Base less than 0 is not allowed)"))
            print("Power=",(a**b))
            con=input("Do you want to continue:(y for yes/any other key for no):")
            if con=='y' or con=='Y':
                ch1=int(input("Enter\n1.Back\n2.Back to Home"))
                if ch1==1:
                    i=1
                elif ch1==2:
                    i=0
                    main()
            else:
                i=0
                print("Thank you for visiting!!!")
        elif ch1==12:
            i=0
            main()
        elif ch1==13:
            i=0
            print("Thank You for visiting!!!")
        else:
            i=1
            print("Invalid choice... Please re-enter your choice:")

def convertor():
    i=1
    while i==1:
        print("Which type of conversion you wish to do:")
        print("1.Currency Convertor\n2.Unit Convertor\n3.Back to Home\n4.Quit")
        ch2=int(input("Enter your choice here:"))
        if ch2==1:
            currency()
            i=0
        elif ch2==2:
            unit()
            i=0
        elif ch2==3:
            main()
            i=0
        elif ch2==4:
            print("Thank you for visiting!!!")
            i=0
        else:
            print("Invalid choice... Please re-enter your choice :")
            i=1        

def statistics():
    i=1
    while i==1:
        print("Which chart would you like to create:")
        print("1.Bar Graph\n2.Histogram\n3.Scatter Plot\n4.Pie Chart\n5.Back to Home\n6.Quit")
        ch3=int(input("Enter your choice here:"))
        if ch3==1:
            bar()
            i=0
        elif ch3==2:
            hist()
            i=0
        elif ch3==3:
            scatter()
            i=0
        elif ch3==4:
            pie()
            i=0
        elif ch3==5:
            main()
            i=0
        elif ch3==6:
            print("Thank you for visiting!!!")
            i=0
        else: 
            print("Invalid choice... Please re-enter your choice :")
            i=1 

def mensuration():
    i=1
    while i==1:
        print("Which shape would you like to find Area/Perimeter/Volume")
        print("1.Circle\n2.Triangle\n3.Rectangle\n4.Square\n5.Solid Cylinder\n6.Cube\n7.Sphere\n8.Cone\n9.Back to Home\n10.Quit")
        m=int(input("Enter your choice here:"))
        if m>0 and m<9:
            if m==1:
                r=float(input("Enter the radius of circle:"))
                print("Area of cirle=",(3.14*r*r),"\nPerimeter of circle=",(2*3.14*r))
                i=0
            elif m==2:
                i=0
                s1=float(input("Enter the length of the base of the triangle:"))
                s2=input("Enter length of second side of the triangle(if known):")
                s3=input("Enter length of third side of the triangle(if known):")
                h=input("Enter the length of the height of the triangle(if known):")
                if s2:
                    s2=float(s2)
                    if s3:
                        s3=float(s3)
                        if h:
                            float(h)
                            print("Area of triangle=",(0.5*s1*h),"\nPerimeter of triangle=",(s1+s2+s3))
                        else:
                            print("Perimeter of triangle=",(s1+s2+s3))
                elif h:
                    h=float(h)
                    print("Area of triangle=",(0.5*s1*h))
                else:
                    print("Incomplete input... Please try again...")
            elif m==3:
                i=0
                l=float(input("Enter the length of rectangle:"))
                b=float(input("Enter the breadth of rectangle:"))
                print("Area of rectangle=",(l*b),"\nPerimeter of rectangle=",(2*(l+b)))
            elif m==4:
                i=0
                a=float(input("Enter the side of square:"))
                print("Area of square=",(a*a),"\nPerimeter of square=",(4*a))
            elif m==5:
                i=0
                r=float(input("Enter the radius of solid cylinder:"))
                h=float(input("Enter the height of solid cylinder:"))
                print("Volume of solid cylinder=",(3.14*r*r*h),"\nCurved surface area of sloid cylinder=",(2*3.14*r*h),"\nTotal Surface Area of Solid Cylinder=",((2*3.14*r*r)+(2*3.14*r*h)))
            elif m==6:
                i=0
                s=float(input("Enter the side of cube:"))
                print("Volume of cube=",(s*s*s),"\nLateral surface area of cube=",(4*s*s),"\nTotal surface area of cube=",(6*s*s))
            elif m==7:
                i=0
                r=float(input("Enter the radius of sphere:"))
                print("Volume of sphere=",(4*3.14*r**3),"Total surface area of sphere=",(4*3.14*r*r))
            elif m==8:
                i=0
                r=float(input("Enter the radius of the cone:"))
                l=input("Enter the slant height of the cone(if known):")
                h=input("Enter the height of the cone(if known):")
                if l:
                    l=float(l)
                    if h:
                        h=float(h)
                        print("Volume of cone=",((3.14*r*r*h)/3),"\nCurved surface area of cone=",(3.14*r*l),"\nTotal surface area of cone=",((3.14*r*l)+(3.14*r*r)))
                    else:
                        print("Curved surface area of cone=",(3.14*r*l),"\nTotal surface area of cone=",((3.14*r*l)+(3.14*r*r)))
                elif h:
                    h=float(h)
                    print("Volume of cone=",((3.14*r*r*h)/3))
                else:
                    print("Incomplete input... Please try again...")
            con=input("Do you want to continue:(y for yes/any other key for no):")
            if con=='y' or con=='Y':
                ch1=int(input("Enter\n1.Back\n2.Back to Home"))
                if ch1==1:
                    i=1
                elif ch1==2:
                    i=0
                    main()
            else:
                i=0
                print("Thank you for visiting!!!")
        elif m==9:
            main()
            i=0
        elif m==10:
            i=0
            print("Thank you for visiting!!!")
        else:
            i=1
            print("Invalid choice... Please re-enter your choice:")    

def currency():
    i=1
    while i==1:
        print("Which currency you want to convert:")
        print("1.US Dollar(USD)\n2.Euro(EUR)\n3.Japanese Yen(JPY)\n4.British Pound(GBP)\n5.Australian Dollar(AUD)\n6.Canadian Dollar(CAD)\n7.Swiss Franc(CHF)\n8.Indian Ruppee(INR)\n9.Swedish Krona(SEK)\n10.Russian Ruble(RUB)\n11.Back\n12.Back to Home\n13.Quit")
        cu1=int(input("Enter your choice here:"))
        if cu1>0 and cu1<11:
            cu2=int(input("Enter the currency into which you want to convert:"))
        if (cu1<11 and cu1>0) and (cu2<11 and cu2>0):
            i=0
            amt=int(input("Enter the amount you want to convert:"))
            if cu1==1:
                if cu2==1:
                    print("USD=",(amt))
                elif cu2==2:
                    print("EUR=",(amt*0.90))
                elif cu2==3:
                    print("JPY=",(amt*109.38))
                elif cu2==4:
                    print("GBP=",(amt*0.773))
                elif cu2==5:
                    print("AUD=",(amt*1.445))
                elif cu2==6:
                    print("CAD=",(amt*1.315))
                elif cu2==7:
                    print("CHF=",(amt*0.982))
                elif cu2==8:
                    print("INR=",(amt*71.19))
                elif cu2==9:
                    print("SEK=",(amt*9.442))
                elif cu2==10:
                    print("RUB=",(amt*63.921))
            elif cu1==2:
                if cu2==1:
                    print("USD=",(amt*1.109))
                elif cu2==2:
                    print("EUR=",(amt))
                elif cu2==3:
                    print("JPY=",(amt*121.324))
                elif cu2==4:
                    print("GBP=",(amt*0.857))
                elif cu2==5:
                    print("AUD=",(amt*1.603))
                elif cu2==6:
                    print("CAD=",(amt*1.459))
                elif cu2==7:
                    print("CHF=",(amt*1.089))
                elif cu2==8:
                    print("INR=",(amt*78.957))
                elif cu2==9:
                    print("SEK=",(amt*10.472))
                elif cu2==10:
                    print("RUB=",(amt*70.895))
            elif cu1==3:
                if cu2==1:
                    print("USD=",(amt*0.0091))
                elif cu2==2:
                    print("EUR=",(amt*0.0082))
                elif cu2==3:
                    print("JPY=",(amt))
                elif cu2==4:
                    print("GBP=",(amt*0.007))
                elif cu2==5:
                    print("AUD=",(amt*0.0132))
                elif cu2==6:
                    print("CAD=",(amt*0.012))
                elif cu2==7:
                    print("CHF=",(amt*0.0089))
                elif cu2==8:
                    print("INR=",(amt*0.6507))
                elif cu2==9:
                    print("SEK=",(amt*0.0863))
                elif cu2==10:
                    print("RUB=",(amt*0.5843))
            elif cu1==4:
                if cu2==1:
                    print("USD=",(amt*1.2935))
                elif cu2==2:
                    print("EUR=",(amt*1.1662))
                elif cu2==3:
                    print("JPY=",(amt*141.496))
                elif cu2==4:
                    print("GBP=",(amt))
                elif cu2==5:
                    print("AUD=",(amt*1.869))
                elif cu2==6:
                    print("CAD=",(amt*1.7014))
                elif cu2==7:
                    print("CHF=",(amt*1.2703))
                elif cu2==8:
                    print("INR=",(amt*92.0842))
                elif cu2==9:
                    print("SEK=",(amt*12.2136))
                elif cu2==10:
                    print("RUB=",(amt*82.6824))
            elif cu1==5:
                if cu2==1:
                    print("USD=",(amt*0.6919))
                elif cu2==2:
                    print("EUR=",(amt*0.6239))
                elif cu2==3:
                    print("JPY=",(amt*75.6978))
                elif cu2==4:
                    print("GBP=",(amt*0.5349))
                elif cu2==5:
                    print("AUD=",(amt))
                elif cu2==6:
                    print("CAD=",(amt*0.9102))
                elif cu2==7:
                    print("CHF=",(amt*0.6796))
                elif cu2==8:
                    print("INR=",(amt*49.26))
                elif cu2==9:
                    print("SEK=",(amt*6.534))
                elif cu2==10:
                    print("RUB=",(amt*44.23))
            elif cu1==6:
                if cu2==1:
                    print("USD=",(amt*0.7602))
                elif cu2==2:
                    print("EUR=",(amt*0.68))
                elif cu2==3:
                    print("JPY=",(amt*83.16))
                elif cu2==4:
                    print("GBP=",(amt*0.587))
                elif cu2==5:
                    print("AUD=",(amt*1.0985))
                elif cu2==6:
                    print("CAD=",(amt))
                elif cu2==7:
                    print("CHF=",(amt*0.7466))
                elif cu2==8:
                    print("INR=",(amt*54.12))
                elif cu2==9:
                    print("SEK=",(amt*7.1782))
                elif cu2==10:
                    print("RUB=",(amt*48.59))
            elif cu1==7:
                if cu2==1:
                    print("USD=",(amt*1.0182))
                elif cu2==2:
                    print("EUR=",(amt*0.918))
                elif cu2==3:
                    print("JPY=",(amt*111.383))
                elif cu2==4:
                    print("GBP=",(amt*0.7871))
                elif cu2==5:
                    print("AUD=",(amt*1.4714))
                elif cu2==6:
                    print("CAD=",(amt*1.3393))
                elif cu2==7:
                    print("CHF=",(amt))
                elif cu2==8:
                    print("INR=",(amt*72.487))
                elif cu2==9:
                    print("SEK=",(amt*9.6143))
                elif cu2==10:
                    print("RUB=",(amt*65.0865))
            elif cu1==8:
                if cu2==1:
                    print("USD=",(amt*0.014))
                elif cu2==2:
                    print("EUR=",(amt*0.0126))
                elif cu2==3:
                    print("JPY=",(amt*1.5365))
                elif cu2==4:
                    print("GBP=",(amt*0.0108))
                elif cu2==5:
                    print("AUD=",(amt*0.0202))
                elif cu2==6:
                    print("CAD=",(amt*0.0184))
                elif cu2==7:
                    print("CHF=",(amt*0.0137))
                elif cu2==8:
                    print("INR=",(amt))
                elif cu2==9:
                    print("SEK=",(amt*0.1326))
                elif cu2==10:
                    print("RUB=",(amt*0.8978))
            elif cu1==9:
                if cu2==1:
                    print("USD=",(amt*0.1059))
                elif cu2==2:
                    print("EUR=",(amt*0.0954))
                elif cu2==3:
                    print("JPY=",(amt*11.585))
                elif cu2==4:
                    print("GBP=",(amt*0.0818))
                elif cu2==5:
                    print("AUD=",(amt*0.153))
                elif cu2==6:
                    print("CAD=",(amt*0.14))
                elif cu2==7:
                    print("CHF=",(amt*0.10))
                elif cu2==8:
                    print("INR=",(amt*7.5394))
                elif cu2==9:
                    print("SEK=",(amt))
                elif cu2==10:
                    print("RUB=",(amt*6.58))
            elif cu1==10:
                if cu2==1:
                    print("USD=",(amt*0.016))
                elif cu2==2:
                    print("EUR=",(amt*0.015))
                elif cu2==3:
                    print("JPY=",(amt*1.77))
                elif cu2==4:
                    print("GBP=",(amt*0.012))
                elif cu2==5:
                    print("AUD=",(amt*0.023))
                elif cu2==6:
                    print("CAD=",(amt*0.021))
                elif cu2==7:
                    print("CHF=",(amt*0.01536))
                elif cu2==8:
                    print("INR=",(amt*1.15))
                elif cu2==9:
                    print("SEK=",(amt*0.15))
                elif cu2==10:
                    print("RUB=",(amt))
            con=input("Do you want to continue:(y for yes/any other key for no):")
            if con=='y' or con=='Y':
                ch1=int(input("Enter\n1.Back\n2.Back to Home"))
                if ch1==1:
                    i=0
                    convertor()
                elif ch1==2:
                    i=0
                    main()
            else:
                i=0
                print("Thank you for visiting!!!")
        elif cu1==11:
            i=0
            convertor()
        elif cu1==12:
            i=0
            main()
        elif cu1==13:
            i=0
            print("Thank you for visiting!!!")
        else:
            i=1
            print("Inavlid choice...Please re-enter ")

def unit():
    i=1
    while i==1:
        print("Which conversion you want to perform:")
        print(" 1.length\n2.time\n3.weight\n4.back\n5.back to home\n6.quit")
        s=int(input("Enter your choice"))
        if s==1:
            i=0
            print("1.m to km\n2.m to inch\n3.m to foot\n4. m to cm\n5.km to m\n6.km to inch\n7.km to foot\n8.inch to m\n9.inch to km\n10.inch to foot\n11.foot to m\n12.foot to km\n13.foot to inch\n14.quit")
            p=int(input("enter your choice"))
            x=int(input("enter the value you want to convert"))
            if p==1:
                a=x*1000000
                print("your conversion ans is",a)
            elif p==2:
                a=x*39.37
                print("your conversion ans is",a)
            elif p==3:
                a=x*3.28
                print("your conversion ans is",a)
            elif p==4:
                a=x*100
                print("your conversion ans is",a)
            elif p==5:
                a=x*1000
                print("your conversion ans is",a)
            elif p==6:
                a=x*39370
                print("your conversion ans is",a)
            elif p==7:
                a=x*3280.83
                print("your conversion ans is",a)
            elif p==8:
                a=x/39.37
                print("your conversion ans is",a)
            elif p==9:
                a=x/39370
                print("your conversion ans is",a)
            elif p==10:
                a=x/12
                print("your conversion ans is",a)
            elif p==11:
                a=x/3.281
                print("your conversion ans is",a)
            elif p==13:
                a=x*12
                print("your conversion ans is",a)
            elif p==12:
                a=x/3281
                print("your conversion ans is",a)
            elif p==14:
                print("Thank you for visiting!!!")    
            con=input("Do you want to continue:(y for yes/any other key for no):")
            if con=='y' or con=='Y':
                ch1=int(input("Enter\n1.Back\n2.Back to Home"))
                if ch1==1:
                    i=0
                    convertor()
                elif ch1==2:
                    i=0
                    main()
            else:
                i=0
                print("Thank you for visiting!!!")
        elif s==2:
            i=0
            print("1.sec to min\n2.sec to hr\n3.min to sec\n4.min to hr\n5.hr to sec\n6.hr to min\n7.quit")
            y=int(input("enter your choice:"))
            x=int(input("enter the value you want to convert:"))
            if y==1:
               a=x/60
               print("your conversion ans is:",a)
            elif y==2:
               a=x/3600
               print("your conversion ans is:",a)
            elif y==3:
                a=x*60
                print("your conversion ans is:",a)
            elif y==4:
                a=x/60
                print("your conversion ans is:",a)
            elif y==5:
                a=x*3600
                print("your conversion ans is:",a)
            elif y==6:
                a=x*60
                print("your conversion ans is:",a)
            elif y==7:
                print("Thank you for visiting!!!")
            con=input("Do you want to continue:(y for yes/any other key for no):")
            if con=='y' or con=='Y':
                ch1=int(input("Enter\n1.Back\n2.Back to Home"))
                if ch1==1:
                    i=0
                    convertor()
                elif ch1==2:
                    i=0
                    main()
            else:
                i=0
                print("Thank you for visiting!!!")

        elif s==3:
            i=0
            print("1.kg to gm\n2.kg to tonnes\n3.kg to ounce\n4.gm to kg\n5.gm to ounce\n6.ounnce to gm\n7.ounce to tonnes\n8.ounce to kg\n9.quit" )
            z=int(input("enter your choice"))
            x=int(input("enter the value you want to convert"))
            if z==1:
                a=x*1000
                print("your ans is",a)
            elif z==2:
                a=x/1000
                print("your ans is ",a)
            elif z==3:
                a=x*35.27
                print("your ans is ",a)
            elif z==4:
                a=x/1000
                print("your ans is ",a)
            elif z==5:
                 a=x/35274
                 print("your ans is ",a)
            elif z==6:
                a=x*28.35
                print("your ans is ",a)
            elif z==7:
                a=x/35274
                print("your ans is ",a)
            elif z==8:
                 a=x/35.274
                 print("your ans is ",a)
            elif z==9:
                print("Thank you for visiting!!!")
            con=input("Do you want to continue:(y for yes/any other key for no):")
            if con=='y' or con=='Y':
                ch1=int(input("Enter\n1.Back\n2.Back to Home"))
                if ch1==1:
                    i=0
                    convertor()
                elif ch1==2:
                    i=0
                    main()
            else:
                i=0
                print("Thank you for visiting!!!")
        elif s==4:
            convertor()
            i=0
        elif s==5 :
            main()
            i=0
        elif s==6:
            print("Thank you for visiting!!!")
            i=0
        else:
            i=1
            print("Invalid choice... Please renter your choice:")

def bar():
    n=int(input("Enter the NUMBER of entries you want to display in the bar graph:"))
    for i in range(1,(n+1)):
        x=int(input("Enter the value on x-axis:"))
        y=int(input("Enter the value on y-axis:"))
        plt.bar([x],[y],label="")
    xlab=input("Enter the label for x-axis(if any):")
    ylab=input("Enter the label for y-axis(if any):")
    if xlab:
        plt.xlabel(xlab)
    else:
        plt.xlabel("X-Axis")
    if ylab:
        plt.ylabel(ylab)
    else:
        plt.ylabel("Y-Axis")
    title=input("Enter the title of the graph(if any):")
    if title:
        plt.title(title)
    else:
        plt.title("Bar Graph")
    plt.legend()
    plt.show()
    con=input("Do you want to continue:(y for yes/any other key for no):")
    if con=='y' or con=='Y':
        ch1=int(input("Enter\n1.Back\n2.Back to Home"))
        if ch1==1:
            statistics()
        elif ch1==2:
            main()
    else:
        print("Thank you for visiting!!!")

def hist():
    x=[0]
    y=[]
    n=int(input("Enter the NUMBER of entries you want to display in the histogram:"))
    for i in range(1,(n+1)):
        x1=int(input("Enter the value on x-axis:"))
        y1=int(input("Enter the value on y-axis:"))
        x.append(x1)
        y.append(y1)
    plt.hist(y,x,histtype='bar')
    xlab=input("Enter the label for x-axis(if any):")
    ylab=input("Enter the label for y-axis(if any):")
    if xlab:
        plt.xlabel(xlab)
    else:
        plt.xlabel("X-Axis")
    if ylab:
        plt.ylabel(ylab)
    else:
        plt.ylabel("Y-Axis")
    title=input("Enter the title of the graph(if any):")
    if title:
        plt.title(title)
    else:
        plt.title("Histogram")
    plt.legend()
    plt.show()
    con=input("Do you want to continue:(y for yes/any other key for no):")
    if con=='y' or con=='Y':
        ch1=int(input("Enter\n1.Back\n2.Back to Home"))
        if ch1==1:
            statistics()
        elif ch1==2:
            main()
    else:
        print("Thank you for visiting!!!")

def scatter():
    x=[]
    y=[]
    n=int(input("Enter the NUMBER of entries you want to display in the Scatter plot:"))
    for i in range(1,(n+1)):
        x1=int(input("Enter the value on x-axis:"))
        y1=int(input("Enter the value on y-axis:"))
        x.append(x1)
        y.append(y1)
    plt.scatter(x,y,s=25,marker='o')
    xlab=input("Enter the label for x-axis(if any):")
    ylab=input("Enter the label for y-axis(if any):")
    if xlab:
        plt.xlabel(xlab)
    else:
        plt.xlabel("X-Axis")
    if ylab:
        plt.ylabel(ylab)
    else:
        plt.ylabel("Y-Axis")
    title=input("Enter the title of the graph(if any):")
    if title:
        plt.title(title)
    else:
        plt.title("Scatter Plot")
    plt.legend()
    plt.show()
    con=input("Do you want to continue:(y for yes/any other key for no):")
    if con=='y' or con=='Y':
        ch1=int(input("Enter\n1.Back\n2.Back to Home"))
        if ch1==1:
            statistics()
        elif ch1==2:
            main()
    else:
        print("Thank you for visiting!!!")

def pie():
    n=int(input("Enter the NUMBER of parts you want to display in pie chart:"))
    slices,activity,exp=[],[],[]
    for i in range(1,(n+1)):
        print("Enter the value of part",i,end="")
        slice=int(input(""))
        slices.append(slice)
        act=input("Enter the corresponding activity to be displayed in the pie chart:")
        activity.append(act)
        exp.append(0)
    plt.pie(slices,labels=activity,startangle=90,shadow=True,explode=exp,autopct='%1.1f%%')
    title=input("Enter the title of the graph(if any):")
    if title:
        plt.title(title)
    else:
        plt.title("Pie Chart")
    plt.show()
    con=input("Do you want to continue:(y for yes/any other key for no):")
    if con=='y' or con=='Y':
        ch1=int(input("Enter\n1.Back\n2.Back to Home"))
        if ch1==1:
            statistics()
        elif ch1==2:
            main()
    else:
        print("Thank you for visiting!!!")

# 
import matplotlib.pyplot as plt
plt.plot([1,1,3.5,6,6],[1,7,4,7,1])
plt.plot([7,9.5,12,11,8],[1,7,1,4,4])
plt.plot([13,18,15.5,15.5],[7,7,7,1])
plt.plot([19,19,19,24,24,24],[7,1,4,4,7,1])
plt.plot([30,25,25,30,30,25],[7,7,4,4,1,1])
plt.plot([38,38,43],[7,1,1])
plt.plot([44,46.5,49,48,45],[1,7,1,4,4])
plt.plot([50,50,55,55,50,55,55,50],[1,7,7,4,4,4,1,1])
plt.show()
print("Hi Guys... Welcome to MATHS LAB...")
main()
