

from functions import get_circle_area, get_sphere_volume



def main():
    """
    Compute area and volume of circle and sphere of radius r.
    """
    try:
        r = float(input("\nEnter radius: "))

    except Exception as ee:
        print(f"Invalid radius entered: str(ee)")

    else:
        area = get_circle_area(r)
        volume = get_sphere_volume(r)

        print(f"\nradius={r}, area={area:.2f}, volume={volume:.2f}\n")




if __name__ == "__main__":

    main()
