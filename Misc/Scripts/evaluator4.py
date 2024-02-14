


def subscription_cost(membership_level):
    if membership_level == "Platinum":
        return 60
    elif membership_level == "Gold":
        return 50
    elif membership_level == "Silver":
        return 40
    elif membership_level == "Bronze":
        return 30
    elif membership_level == "Free Trial":
        return 0



def main():
    answer = input("Would you like to sign up for our monthly membership box?(yes/no): ")
    if answer.lower() == "yes":
        membership_level = input("Please choose your membership level (Platinum, Gold, Silver, Bronze, Free Trial): ")
        cost = subscription_cost(membership_level)
        print(f"The cost for {membership_level} membership is ${cost}.")
    else:
        print("Thank you! Come back if you change your mind.")


if __name__ == "__main__":
    main()