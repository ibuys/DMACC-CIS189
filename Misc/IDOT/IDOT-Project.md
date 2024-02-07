
## IDOT Mini-Project

You've been contracted by the Iowa Department of Transportation (IDOT) to automate 
the calculation of fines for overweight vehicles traveling on the interstate. 


**Project Requirements:**

- The vehicle type can be either "car", "suv" or "semi".

    - If vehicle type is car or suv, no fine is levied (fine = $0)

    - If vehicle type is semi, prompt the driver to enter:

        1. Whether they are driving a single, double or triple axle semi.

        2. The total vehicle weight (let's assume we can trust them).

            - The weight limits are:

                - 20,000lbs. for single axle
                - 35,000lbs. for double axle
                - 50,000lbs. for triple axle

        - The driver is fined $1 for every pound over the limit up to a maximum of $10,000. 
          For example, a triple axle semi carrying 65,000 lbs. should be fined $10,000,
          not $15,000.

        - The minimum fine is $500. For example, if a single axle semi is carrying 
          20,001 lbs., they should be fined $500, not $1. 

        - Separate from the overweight fine, if a semi is overweight by more than 
          1,000 lbs., an $25 donation to Ducks Unlimited is required. 


The task is to prompt the driver for their vehicle type, and determine the total
fine amount (plus $25 donation when applicable) for semis based on the number 
of axles and total weight. Notice that when the $25 donation is applied, 
an additional print statement must be output (see Example 3).


- Download `template.py` from canvas, and rename the file with your team name. 

- The project lead has the final decision on any design disputes. They
are also responsible for emailing the .py file. 

- **Everyone in the group must participate**. It is the responsibility of the 
project lead to ensure that everyone on the team understands each line of code
in the submitted script. I will randomly call on one person from each team to 
briefly walk through the code, so make sure everyone can explain it. 


- **Deliverable:**: Email a .py script with your team name to jdtriveri@dmacc.edu. The deadline
is 8:10pm.


**Hint:** 
The fact that dollars and pounds are on a 1-to-1 basis should make the 
conditions in your `if/elif/else` blocks straightforward to setup. 



    
## Test cases to validate your code against

```
# Example 1 (non-semi):
(prompt) Enter vehicle type (car, suv, semi): suv
(output) Total fine: $0

# Example 2 (semi, overage less than 1000lbs.):
(prompt) Enter vehicle type: semi
(prompt) Enter number of axles (single, double, triple): triple
(prompt) Enter vehicle weight (lbs.): 50750
(output) Overage: 750lbs., Total fine: $750

# Example 3 (semi, overage greater than 1000 lbs.):
(prompt) Enter vehicle type: semi
(prompt) Enter number of axles (single, double, triple): double
(prompt) Enter vehicle weight (lbs.): 42500
(output) Overage: 7500lbs., Total fine: $7525
(output) Ducks Unlimited appreciates your support!!!

# Example 4 (semi, no overage):
(prompt) Enter vehicle type: semi
(prompt) Enter number of axles (single, double, triple): single
(prompt) Enter vehicle weight (lbs.): 19000
(output) Overage: -1,000lbs., Total fine: $0

# Example 5 (semi, overage greater than 10000):
(prompt) Enter vehicle type: semi
(prompt) Enter number of axles (single, double, triple): double
(prompt) Enter vehicle weight (lbs.): 60000
(output) Overage: 25000lbs., Total fine: $10000
```