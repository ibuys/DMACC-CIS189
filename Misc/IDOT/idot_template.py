"""
The task is to prompt the driver for their vehicle type, and determine the total
fine amount (plus $25 donation when applicable) for semis based on the number 
of axles and total weight. Notice that when the $25 donation is applied, 
and additional print statement must be displayed.
"""

# Declare constants for max allowable weight by number of axles, as well as
# minimum and maximum fine, and Ducks Unlimited donation. 
SINGLE_AXLE_MAX = 20000
DOUBLE_AXLE_MAX = 35000
TRIPLE_AXLE_MAX = 50000
MINIMUM_FINE = 500
MAXIMUM_FINE = 10000
DUCKS_ULMTD_DONATION_AMOUNT = 25


vehicle_type = input("Enter vehicle type (car|suv|semi): ")

if vehicle_type != "semi":
    print("Total fine: $0")


else:

    # Prompt for number of axles.
    # nbr_axles = 



    # Prompt for total weight.
    # total_weight = 



    # Determine overage based on nbr_axles and total_weight.



    # Determine levy_amount based on where overage falls between 0 and MAXIMUM_FINE.



    # Check to see if overage exceeds 1000. If so, add $25 Ducks Unlimited
    # donation, and display "Ducks Unlimited appreciates your support!".
    # Otherwise, just print overage and total fine. 
    


    # Remove pass prior to submitting. Used as a placeholder.
    pass
