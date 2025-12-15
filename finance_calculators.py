#investiment and loan repayment calculator programmes
import math
#main menu display 
#user input choice
print("investment - to calculate the amount of interest you'll earn on your investment")
print("loan - to calculate the amount you'll have to pay on a home loan")
display_menu=input("Enter either 'investment' or 'loan' from the menu above to proceed: ").lower()
if display_menu=="investment":
    #user inputs for investment calculation
    deposit=int(input("Enter the amount you are depositing: "))
    interest_rate=float(input("Enter the interest rate (as a percentage): "))
    years=int(input("Enter the number of years you plan to invest: "))
    interest_type=input("Enter the type of interest ('simple' or 'compound'): ").lower()
    #simple intrest calculation
    if interest_type=="simple":
        total_amount=deposit*(1+(interest_rate/100)*years)
        print("The total amount after",years,"years with simple interest","is:",round(total_amount,2))
        #compound intrest calculation
    elif interest_type =="compound":
        total_amount=deposit*math.pow((1+(interest_rate/100)),years)
        print("The total amount after",years,"years with compound interest","is:",round(total_amount,2))
    else:
        print("please select correct intrest type")
elif display_menu=="loan":
    #user inputs for loan repayment calculation
    principal=int(input("Enter the present value of the house: "))
    annual_interest_rate=float(input("Enter the annual interest rate (as a percentage): "))
    months=int(input("Enter the number of months you plan to take to repay the loan: "))
    monthly_interest_rate=(annual_interest_rate/100)/12
    #monthly repayment calculation
    monthly_repayment=(principal*monthly_interest_rate)/(1-(1+monthly_interest_rate)**(-months))
    print("Your monthly repayment amount is:",round(monthly_repayment,2))
else:
    print("please select a valid option from the menu")
#end

    
    
