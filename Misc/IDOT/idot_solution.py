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
    nbr_axles = input("Enter number of axles (single|double|triple): ")

    # Prompt for weight.
    total_weight = float(input("Enter vehicle weight (lbs.): "))

    # Determine total overage based on nbr_axles and total_weight.
    if nbr_axles == "single":
        overage = total_weight - SINGLE_AXLE_MAX
    
    elif nbr_axles == "double":
        overage = total_weight - DOUBLE_AXLE_MAX

    elif nbr_axles == "triple":
        overage = total_weight - TRIPLE_AXLE_MAX

    # Determine levy_amount based on where overage falls between 0 and MAXIMUM_FINE.
    if overage <= 0:
        # If overage is less than 0, no fine is levied. 
        levy_amount = 0
    
    elif 0 < overage <= MINIMUM_FINE:
        # If overage is between 0 and minimum fine, levy MINIMUM_FINE.
        levy_amount = MINIMUM_FINE

    elif MINIMUM_FINE < overage <= MAXIMUM_FINE:
        # If overage is between MINIMUM_FINE and MAXIMUM_FINE,
        # levy_amount = overage. 
        levy_amount = overage

    else:
        # If overage exceeds 10,000, levy_amount = MAXIMUM_FINE.
        levy_amount = MAXIMUM_FINE

    # Check to see if overage exceeds 1000. If so, add $25 Ducks Unlimited
    # donation.
    if overage > 1000:
        levy_amount = levy_amount + DUCKS_ULMTD_DONATION_AMOUNT
        print(f"Overage: {overage:,.0f}, Total fine: ${levy_amount:,.0f}.")
        print("Ducks Unlimited appreciates your support!")

    else:
        # No Ducks Unlimited donation. Just print levy_amount.
        print(f"Overage: {overage:,.0f}, Total fine: ${levy_amount:,.0f}.")
